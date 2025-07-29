from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Question
from app.schemas import QuestionCreate
from app import models


async def create_question(data: QuestionCreate, db: AsyncSession) -> Question:
    question = Question(document_id=data.document_id, question=data.question)
    db.add(question)
    await db.commit()
    await db.refresh(question)
    return question


async def update_question_answer(question_id: int, answer: str, db: AsyncSession):
    result = await db.execute(select(models.Question).where(models.Question.id == question_id))
    question = result.scalar_one_or_none()

    if question:
        question.answer = answer
        question.status = "answered"
        await db.commit()
        await db.refresh(question)


async def get_question_by_id(question_id: int, db: AsyncSession):
    result = await db.execute(select(models.Question).where(models.Question.id == question_id))
    return result.scalar_one_or_none()