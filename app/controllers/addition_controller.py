# app/controllers/addition_controller.py
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List
from app.schemas.addition_schema import Input_model, Response_model
from app.services.addition_service import process_additions
import logging

router = APIRouter()

@router.post("/add", response_model=Response_model)
def add(request: Input_model):
    try:
        started_at = datetime.now()
        results = process_additions(request.payload)
        completed_at = datetime.now()
        response = Response_model(
            batchid=request.batchid,
            response=results,
            status="completed",
            started_at=started_at,
            completed_at=completed_at
        )
        return response
    except Exception as e:
        logging.error(f"An error occurred while processing the addition requests: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
