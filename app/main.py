from fastapi import FastAPI
from pydantic import BaseModel
import logging
import multiprocessing
from datetime import datetime

app = FastAPI()

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Input data validation
class Input_model(BaseModel):
    batchid: str
    payload: list[list[int]]

# Response data validation
class Response_model(BaseModel):
    batchid: str
    response: list[int]
    status: str
    started_at: datetime
    completed_at: datetime

def add_list(input_list: list[list[int]]) -> int:

    try:
        res = [sum(ll) for ll in input_list]
        return res
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return []

@app.post("/addition/", response_model=Response_model)
async def perform_addition(request: Input_model):

    try:
        # start time
        started_at = datetime.now()

        # multiprocessing
        pool = multiprocessing.Pool()

        results = pool.apply(add_list, (request.payload,))
        pool.close()
        pool.join()

        # completion time
        completed_at = datetime.now()

        response = {
            "batchid": request.batchid,
            "response": results,
            "status": "complete",
            "started_at": started_at,
            "completed_at": completed_at
        }

        return response
		
    except Exception as e:
        logger.error(f"Error occurred during addition: {e}")
