from enum import Enum
from pydantic import BaseModel, Field

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(str, Enum):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"

class Ticket(BaseModel):
    id: int
    subject: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., min_length=25, max_length=500)
    owner: str = Field(..., min_length=2, max_length=30)
    priorty: Priority = medium
    status: Status = not_started
