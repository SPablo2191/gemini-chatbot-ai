from pydantic import BaseModel

class GeminiQuery(BaseModel):
    messageContent : str