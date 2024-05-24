from pydantic import BaseModel
from typing import List
from datetime import datetime

class Input_model(BaseModel):
    batchid: str
    payload: List[List[int]]

class Response_model(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
