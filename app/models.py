from pydantic import BaseModel

class GeminiQuery(BaseModel):
    question : str