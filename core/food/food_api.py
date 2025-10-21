import requests
from ai.food_analyzer import analyze_ingredient  

API_URL = "http://localhost:8010"


def get_recipe(ingredient, token):
    # ------------------- Check login -------------------
    if not token:
        return "⚠️ Please log in first before searching for recipes."

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{API_URL}/foods/{ingredient}", headers=headers)

    if resp.status_code != 200:
        return f"❌ Error: {resp.json().get('detail', 'Unauthorized')}"

    data = resp.json()

    # ------------------- Extract recipes -------------------
    recipes = (
        data.get("recipes")
        or data.get("results")
        or data.get("recipe")
        or []
    )

    if isinstance(recipes, dict):
        inner = recipes.get("meals") or recipes.get("items")
        recipes = inner if isinstance(inner, list) else [recipes]

    if not isinstance(recipes, list) or not recipes:
        return f"⚠️ No recipes found for '{ingredient}'."

    result_texts = []

    for recipe in recipes:
        name = recipe.get("name") or recipe.get("strMeal") or "Unknown Recipe"
        category = recipe.get("category") or recipe.get("strCategory") or "Unknown"
        area = recipe.get("area") or recipe.get("strArea") or "Unknown"
        instructions = recipe.get("instructions") or recipe.get("strInstructions") or "No instructions available."
        thumbnail = recipe.get("thumbnail") or recipe.get("strMealThumb") or "No image available"
        video = recipe.get("video") or recipe.get("strYoutube")

        result_texts.append(
            f"\n\n###  recipe for **{ingredient.title()}**\n"
            f"🍽️ **{name}**  \n"
            f"📂 Category: {category}  \n"
            f"🌍 Area: {area}  \n\n"
            f"📖 **Instructions:**  \n{instructions}\n\n"
            f"🖼️ [Click to View Image]({thumbnail})  \n"
            f"{'🎥 [Click to Watch Video](' + video + ')  \n' if video else ''}"    
            f"---\n"
        )

    # ------------------- Nutrition Info -------------------
    nutrition = analyze_ingredient(ingredient)

    if "error" not in nutrition:
        nutrition_text = (
            f"\n\n### 🥦 Nutrition Info for **{ingredient.title()}**\n"
            f"📏 Amount: {nutrition.get('amount', 'N/A')}  \n"
            f"🔥 Calories: {nutrition.get('calories', 'N/A')} kcal  \n"
            f"💪 Protein: {nutrition.get('protein', 'N/A')} g  \n"
            f"🥑 Fat: {nutrition.get('fat', 'N/A')} g  \n"
            f"🍞 Carbohydrates: {nutrition.get('carbohydrates', 'N/A')} g  \n"
        )
    else:
        nutrition_text = "\n\n⚠️ Could not retrieve nutrition information."

    return nutrition_text + "\n\n" + "\n\n".join(result_texts) 
