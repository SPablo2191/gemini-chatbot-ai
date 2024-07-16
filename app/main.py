from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import GeminiQuery
from app.config import model


app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/question")
async def ask(data: GeminiQuery):
    response = model.generate_content(data.messageContent)
    return {"message": response.text}
