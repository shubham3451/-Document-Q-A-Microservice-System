import asyncio
import httpx
import os
import logging
from app.services import update_question_answer
from app.db import SessionLocal


logger = logging.getLogger(__name__)
DOCUMENT_SERVICE_URL = os.getenv("DOCUMENT_SERVICE_URL", "http://document_service:8001")


async def generate_answer(question_id: int, question_text: str, document_id: int):
    logger.info(f"⏳ Background task started for question {question_id}")
    async with SessionLocal() as db: 
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{DOCUMENT_SERVICE_URL}/documents/{document_id}")
                if response.status_code != 200:
                    logger.error(" Failed to fetch document content")
                    await update_question_answer(question_id, "Document fetch failed", db)
                    return

            doc = response.json()
            content = doc.get("content", "")

            await asyncio.sleep(5)

            dummy_answer = f"This is a generated answer to your question: '{question_text}'.\nExcerpt: {content[:100]}..."
            await update_question_answer(question_id, dummy_answer, db)
            logger.info(f" Answer generated and saved for question {question_id}")

        except Exception as e:
            logger.exception(f" Exception in background task for question {question_id}: {e}")
