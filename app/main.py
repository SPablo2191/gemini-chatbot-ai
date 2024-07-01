from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
import os
from app.models import GeminiQuery

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
app = FastAPI()
origins = [
    "http://localhost:61224",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/question")
async def ask(data: GeminiQuery):
    response = model.generate_content(data.messageContent)
    return {"message": response.text}
