# ai/food_analyzer.py
from openai import OpenAI
import os
import json

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ingredient(ingredient_name: str) -> dict:
    """
    Input: ingredient name (e.g., "potato")
    Output: dictionary with nutrition info
    """

    prompt = f"""
    You are a nutrition expert.
    Please provide nutritional information for '{ingredient_name}' per 1 serving.

    Respond ONLY in JSON with the following structure:
    {{
        "amount": "100 grams",
        "calories": 120,
        "protein": 2,
        "fat": 0.5,
        "carbohydrates": 27
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert nutritionist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        answer = response.choices[0].message.content.strip()

        # Extract JSON from model output
        json_start = answer.find("{")
        json_end = answer.rfind("}") + 1
        json_str = answer[json_start:json_end]

        data = json.loads(json_str)
        return data  

    except Exception as e:
        return {"error": str(e)}
