from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app import schemas, services
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/documents/", response_model=schemas.DocumentOut)
async def create_document(doc: schemas.DocumentCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating document: {doc.title}")
    return await services.create_document(doc, db)

@router.get("/documents/{doc_id}", response_model=schemas.DocumentOut)
async def read_document(doc_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Fetching document ID {doc_id}")
    document = await services.get_document(doc_id, db)
    if not document:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Document not found")
    return document

@router.get("/health")
async def health():
    return {"status": "document_service ok"}
