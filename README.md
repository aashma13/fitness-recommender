## GPT-4 Based Fitness Workout & Meal Plan Recommender App

A personalized fitness and nutrition assistant powered by GPT-4 and semantic vector search (FAISS). This AI-driven app provides **customized weekly workout routines and diet plans** tailored to your fitness goals, dietary preferences, and health profile. It uses **LLM-based embeddings** to match users with optimal meal plans and workouts using **semantic similarity search**.





https://github.com/user-attachments/assets/76fa5759-e6cc-4b56-a0e3-9e8513c74503





<img src="https://github.com/aashma13/fitness-recommender/blob/7206a123081b6a31aba7e8f4b62133ae9b04807e/fintess_and_meal_plans.mp4.gif">

---

### Features

* **GPT-4 Powered Recommendations**
  Uses GPT-4 to generate and personalize fitness and dietary guidance based on user input.

* **Semantic Search with FAISS**
  Meal and workout recommendations are retrieved via **vector similarity** using FAISS and OpenAI embeddings, enabling context-aware and personalized results based on previous other users goal. 

* **User Profile-Based Personalization**

* **Weekly Planner**
  Outputs structured **7-day plans** for both workouts and meals.

* **Meal Database with Nutritional Info**
  workouts and diet data form other data stored by Gym center. 

---

### Tech Stack

* **Backend**: Python, FastAPI
* **LLM**: OpenAI GPT-4 (via API)
* **Embeddings**: OpenAI Embeddings (e.g., `text-embedding-3-small`)
* **Vector Search**: FAISS
* **Frontend**: Streamlit
* **Deployment**: Docker

---

### Example Workflow

1. **User signs up** and fills in a profile (age, gender, height, weight, fitness goal, dietary preferences).
2. **App encodes the profile and context** into an embedding.
3. **FAISS searches** the meal/workout vector database for semantically similar items.
4. **GPT-4 curates a 7-day plan** using the retrieved items, ensuring logical structure and balance.
5. **The user receives a detailed, personalized plan** that includes meal  and daily workouts.


## Setup & Run Guide

### Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (a drop-in replacement for pip + venv)

---

### 1. Clone & Navigate

```bash
git clone <your-repo-url>
cd fitnessapp
````

---

### 2. Install `uv` (if not already installed)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Or with pipx:

```bash
pipx install uv
```

---

### 3. Create Virtual Environment

```bash
uv venv
```

optional

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
uv pip install -r pyproject.toml
```

---


_Before Running Make sure you have `.env` file_

```.env
OPENAI_API_KEY=sk-proj-as......
```

### 5. Run the Application

```bash
uv run main.py
```

This will start the server on:

```
http://0.0.0.0:9000
```

* Open docs: `http://127.0.0.1:9000/docs`
* Test endpoint: `POST /predict`

---

## Docker Support

### Build Docker Image

```bash
docker build -t fitnessapp .
```

### Run Docker Container

```bash
docker run --env-file .env -p 9000:9000 fitnessapp
```

### use dockercompose (Optionaly)

```bash
docker-compose up --build

```


```bash
docker-compose down

```

---

## Project Structure

```
.
├── api.py
├── dockerfile
├── fitness_data_embedding.pickle
├── __init__.py
├── llm.py
├── main.py
├── pyproject.toml
├── README.md
├── req.json
├── utils.py
├── uv.lock
├── .env
```

---

## Notes

* Ensure you have an OpenAI API key configured if the app makes external API calls.
* The app starts with `uv run`, which behaves like `uvicorn main:app --reload` behind the scenes if your `main.py` defines `app`.


## Running streamlit webapp

```bash
streamlit run app.py
```

### Example Fitness goal:

```
User Fitness Profile
Age: 55–64
Gender: Female
Height: 5'0" – 5'4" (152–163 cm)
Current Weight: 150–174 lbs (68–79 kg)
Desired Weight: 100–124 lbs (45–56 kg)
BMI: 25–29.9 (Overweight)
Occupation Activity Level: Mostly sedentary (desk work/administrative)
Chronic Health Conditions: None
Dietary Preference: Vegetarian
Sleep Duration: 4–5 hours per night
Current Fitness Level: Intermediate
Current Exercise Frequency: Daily
Preferred Update Frequency: Daily
```
