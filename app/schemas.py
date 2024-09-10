from pydantic import BaseModel


class SMessages(BaseModel):
    id: int
    message: str
