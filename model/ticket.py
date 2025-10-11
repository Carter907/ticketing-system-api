from pydantic import BaseModel


class Ticket(BaseModel):
    id: int
    subject: str
    description: str | None = None
    status: str
