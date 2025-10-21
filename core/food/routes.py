
from fastapi import APIRouter, Depends, HTTPException, status
import requests
import random
from user.models import UserModel
from auth.jwt_auth import get_authenticated_user

router = APIRouter(prefix="/foods", tags=["foods"])

@router.get("/{food_name}")
async def read_food(food_name: str, user: UserModel = Depends(get_authenticated_user)):
    
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_name}"
    resp = requests.get(url)
    data = resp.json()

    if not data or data.get("meals") is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No recipes found for '{food_name}'."
        )

    meals = data["meals"]

    recipes = []
    for meal in meals:
        recipes.append({
            "name": meal.get("strMeal"),
            "category": meal.get("strCategory"),
            "area": meal.get("strArea"),
            "instructions": meal.get("strInstructions"),
            "thumbnail": meal.get("strMealThumb"),
            "video": meal.get("strYoutube"), 
        })

    if len(recipes) > 5:
        recipes = random.sample(recipes, 5)

    return {"user": user.username, "recipes": recipes}


