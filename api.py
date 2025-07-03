from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel
from llm import get_embedding, get_combined_context, predict_workout_plan
from utils import ObjectCache
import pandas as pd
import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QueryRequest(BaseModel):
    uid: str
    question: str


object_cache = ObjectCache()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    try:
        object_cache.load_object()
        logger.info("Model loaded successfully at startup.")
    except Exception as e:
        logger.error(f"Failed to load the model on startup: {e}")
    
    yield

    # Clean up cached model
    object_cache.cached_object = None
    logger.info("Cleaned up cached model on shutdown.")


app = FastAPI(lifespan=lifespan)


@app.get("/health_check")
async def health_check():
    return {"message": "VFA app is running"}


@app.post("/predict")
async def predict(request: QueryRequest):
    """Handles workout plan prediction based on user query."""
    try:
        model = object_cache.get_object()
    except Exception as e:
        logger.error(f"Error accessing model: {e}")
        raise HTTPException(status_code=500, detail="Model could not be loaded.")

    try:
        # Step 1: Embed user question
        user_input = request.question
        query_embedding = get_embedding(user_input)

        # Step 2: Retrieve nearest samples
        scores, samples = model.get_nearest_examples("embeddings", np.array(query_embedding), k=5)
        samples_df = pd.DataFrame.from_dict(samples)

        # Step 3: Clean and sort samples
        samples_df.drop(columns=["embeddings"], inplace=True, errors="ignore")
        samples_df["scores"] = scores
        samples_df.sort_values("scores", ascending=False, inplace=True)

        # Step 4: Generate context and predict
        context = get_combined_context(samples_df)
        response = predict_workout_plan(question=user_input, context=context)

        return {
            "uid": request.uid,
            "recs": response
        }

    except Exception as e:
        logger.exception("Prediction failed.")
        raise HTTPException(status_code=500, detail="Failed to process the request.")
