from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class QuestionCreate(BaseModel):
    document_id: int = Field(..., gt=0, description="ID of the document being referenced (positive integer)")
    question: str = Field(..., min_length=5, max_length=500, description="The question asked about the document")

class QuestionOut(BaseModel):
    id: int
    document_id: int
    question: str
    answer: Optional[str] = Field(None, description="The generated answer")
    status: str = Field(..., description="Status must be 'pending' or 'answered'")
    created_at: datetime = Field(..., description="Timestamp when question was created")

    model_config = {
        "from_attributes": True
    }

