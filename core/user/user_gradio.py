
# user_gradio.py
import gradio as gr
import requests


#API_URL = "http://backend:8010"

API_URL = "http://localhost:8010"



# ---------------- User API ----------------
def login(username, password):
    resp = requests.post(
        f"{API_URL}/users/login",
        json={"username": username, "password": password}
    )
    if resp.status_code == 200:
        data = resp.json()
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")
        return " Login successful! Tokens saved.", access_token, refresh_token
    return f" {resp.json().get('detail', 'Login failed')}"


def register(username, password, password_confirm):
    resp = requests.post(
        f"{API_URL}/users/register",
        json={
            "username": username,
            "password": password,
            "password_confirm": password_confirm
        }
    )
    return resp.json()


def refresh(token):
    resp = requests.post(
        f"{API_URL}/users/refresh_token",
        json={"token": token}
    )
    if resp.status_code == 200:
        return " Token refreshed!", resp.json().get("access_token")
    return f" {resp.json().get('detail', 'Failed')}", ""


# ---------------- Food API ----------------
def get_recipe(ingredient, token):
    if not token:
        return " Please login first to access recipes."
    
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{API_URL}/foods/{ingredient}", headers=headers)

    if resp.status_code != 200:
        return f" Error: {resp.json().get('detail', 'Unauthorized')}"
    
    data = resp.json()["recipe"]
    return (
        f"🍽️ **{data['name']}**\n"
        f"📂 Category: {data['category']}\n"
        f"🌍 Area: {data['area']}\n\n"
        f"📖 Instructions:\n{data['instructions']}\n\n"
        f"🖼️ Image: {data['thumbnail']}"
    )


# ---------------- Gradio Blocks ----------------
with gr.Blocks() as demo:
    gr.Markdown("## 👤 User Management & 🍽️ Food Recipes")

    access_token_state = gr.State("")
    refresh_token_state = gr.State("")

    # ---------- Register ----------
    with gr.Tab("Register"):
        u_reg = gr.Textbox(label="Username")
        p_reg = gr.Textbox(label="Password", type="password")
        p_conf = gr.Textbox(label="Confirm Password", type="password")
        out_reg = gr.Textbox(label="Response")
        btn_reg = gr.Button("Register")
        btn_reg.click(register, inputs=[u_reg, p_reg, p_conf], outputs=out_reg)

    # ---------- Login ----------
    with gr.Tab("Login"):
        u_log = gr.Textbox(label="Username")
        p_log = gr.Textbox(label="Password", type="password")
        out_log = gr.Textbox(label="Response")
        btn_log = gr.Button("Login")
        btn_log.click(
            login,
            inputs=[u_log, p_log],
            outputs=[out_log, access_token_state, refresh_token_state]
        )

    # ---------- Refresh Token ----------
    with gr.Tab("Refresh Token"):
        out_token = gr.Textbox(label="Response")
        btn_token = gr.Button("Refresh")
        btn_token.click(
            refresh,
            inputs=refresh_token_state,  
            outputs=[out_token, access_token_state]
        )

    # ---------- Food Recipes ----------
    with gr.Tab("Food Recipes"):
        ingredient = gr.Textbox(label="Food or Ingredient")
        food_out = gr.Textbox(lines=10, label="Recipe")
        btn_food = gr.Button("Get Recipe")
        btn_food.click(get_recipe, inputs=[ingredient, access_token_state], outputs=food_out)


