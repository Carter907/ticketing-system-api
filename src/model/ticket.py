from pydantic import BaseModel, Field


class Ticket(BaseModel):
    id: int
    subject: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., min_length=25, max_length=500)
    status: str
