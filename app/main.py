from fastapi import FastAPI, Depends
import google.generativeai as genai
from dotenv import load_dotenv
import os

from app.models import GeminiQuery

load_dotenv()
print(f"mi key => {os.environ.get('GEMINI_API_KEY', '')}")
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
model = genai.GenerativeModel("gemini-1.5-flash")
app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.post("/question")
def ask_kitten(data: GeminiQuery = Depends()):
    response = model.generate_content(data.question)
    return {"message": response.text}
