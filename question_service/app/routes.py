from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.ext.asyncio import AsyncSession
import httpx
import os
from app import schemas, services, background
from app.db import get_db

router = APIRouter()
DOCUMENT_SERVICE_URL = os.getenv("DOCUMENT_SERVICE_URL")


@router.get("/health")
async def health_check():
    return {"status": "question_service ok"}


@router.post("/questions/", response_model=schemas.QuestionOut)
async def ask_question(
    payload: schemas.QuestionCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DOCUMENT_SERVICE_URL}/documents/{payload.document_id}")
        if response.status_code != 200:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Document does not exist.")

    question = await services.create_question(payload, db)

    background_tasks.add_task(
        background.generate_answer,
        question.id,
        question.question,
        question.document_id
    )

    return question


@router.get("/questions/{question_id}", response_model=schemas.QuestionOut)
async def get_question(question_id: int, db: AsyncSession = Depends(get_db)):
    question = await services.get_question_by_id(question_id, db)
    if not question:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Question not found.")
    return question
