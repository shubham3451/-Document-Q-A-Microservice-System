from pydantic import BaseModel, Field

class DocumentCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200, description="Title of the document (3-200 characters)")
    content: str = Field(..., min_length=10, description="Full text content of the document (minimum 10 characters)")

class DocumentOut(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }

