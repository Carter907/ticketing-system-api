from fastapi import FastAPI, Header
from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    subject: str
    description: str | None = None
    status: str

app = FastAPI()

@app.post("/tickets/create")
def read_item(
    bingus_type: str = Header(),
    content_type: str = Header(),
    ticket: Ticket = Ticket(id=0, subject="[insert subject]", status="not started")
    ):
    print(f"The content type is {content_type}")
    print(f"The bingus type (LOL) is {bingus_type}")
    return ticket