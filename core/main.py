
from contextlib import asynccontextmanager
from fastapi import FastAPI, Response
import gradio as gr
from user.user_gradio import demo 


from user.routes import router as user_router
from food.routes import router as food_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")   
    yield                          
    print("Application shutdown")

tags_metadata = [
     {
        "name": "users",
        "description": "Manage users, authentication, and profiles."
    },
    {
        "name": "foods",
        "description": "Search about food recipes."
    }
   
]  

app = FastAPI(
    title="Food Recipe Application",
    lifespan=lifespan,
    openapi_tags=tags_metadata,
    contact={
        "name":"Fatemeh",
        "email":"abidizadeganfateme@gmail.com"
    }
)
# add routes
app.include_router(food_router)
app.include_router(user_router)

 # add gradios
app = gr.mount_gradio_app(app, demo, path="/")


# from pydantic import BaseModel
# from ai.food_analyzer import analyze_ingredient


# class IngredientRequest(BaseModel):
#     ingredient_name: str

# @app.post("/ingredient_info")
# def get_ingredient_info(data: IngredientRequest):
#     result = analyze_ingredient(data.ingredient_name)
#     return {"ingredient": data.ingredient_name, "info": result}