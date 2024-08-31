from pydantic import BaseModel

class Climb(BaseModel):
    title: str
    content: str