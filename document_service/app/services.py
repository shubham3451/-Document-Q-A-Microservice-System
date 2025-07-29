from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Document
from app.schemas import DocumentCreate

async def create_document(doc_data: DocumentCreate, db: AsyncSession) -> Document:
    document = Document(**doc_data.dict())
    db.add(document)
    await db.commit()
    await db.refresh(document)
    return document

async def get_document(doc_id: int, db: AsyncSession) -> Document | None:
    result = await db.execute(select(Document).where(Document.id == doc_id))
    return result.scalar_one_or_none()
