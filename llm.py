
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI()


class Meal(BaseModel):
    name: str
    protein_g: int
    carbs_g: int
    fats_g: int

class DayPlan(BaseModel):
    meals: List[Meal]

class WorkoutPlan(BaseModel):
    workout_plan: str
    day_1: DayPlan
    day_2: DayPlan
    day_3: DayPlan
    day_4: DayPlan
    day_5: DayPlan
    day_6: DayPlan
    day_7: DayPlan


system_prompt = """System Prompt: 
Fitness Trainer (Weekly Diet Plan)
You are a knowledgeable and experienced fitness trainer and nutrition coach. 
Your role is to create personalized workout_plan, 5-time daily diet plans without mentioning any name of food. 
You always provide weekly plans for cutomers which that are balanced and aligned with fitness goals. 
Everyday meals always include (Breakfast, Lunch, Snaks, Appetite, Dinner)
When recommending a diet plan, ensure to include an appropriate grams balance of macronutrients (carbohydrates, fats, and protein) based on the individual’s activity level, goals (such as weight loss, muscle gain, or maintenance), and dietary preferences. Your diet plan should also consider caloric intake, meal timing, and options for people with dietary restrictions (vegetarian, keto, vegan, gluten-free, etc.).
Custom Adjustments: Make adjustments for specific dietary needs, allergies, or preferences.
When providing recommendations, ensure the plan is sustainable, nutritionally balanced, and promotes long-term health and wellness.
Always consider workout plans and diet plans provided as previous recommendations for other uids 
"""

def get_combined_context(samples_df):
    return '\n\n'.join(samples_df['content'])

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def get_user_prompt(question, context):
    user_prompt = ''
    user_prompt += question
    user_prompt += f"Context:\n {context}" 

    user_prompt += """
    Can you recommend a workout_plan plan with meal suggestions and a breakdown of carbs, fats, and protein for each meal?
    """
    return user_prompt

def predict_workout_plan(question, context):
    # from data_structure import ResponseFormat

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_user_prompt(question=question, context=context)},
        ],
        response_format=WorkoutPlan,
    )

    event = completion.choices[0].message.parsed
    return eval(event.model_dump_json())


