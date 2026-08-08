from pydantic import BaseModel, Field 
from datetime import date, datetime 
from typing import Optional 
from uuid import UUID 
 
class FeedbackBase(BaseModel): 
    beneficiary_id: UUID 
    program_id: UUID 
    feedback_date: date 
    satisfaction_score: int = Field(..., ge=1, le=5, description="Rating from 1 to 5") 
    training_quality: int = Field(..., ge=1, le=5, description="Rating from 1 to 5") 
    comments: Optional[str] = None 
    suggestions: Optional[str] = None 
    follow_up_required: bool = False 
 
class FeedbackCreate(FeedbackBase): 
    pass 
 
class FeedbackResponse(FeedbackBase): 
    id: UUID 
    created_at: datetime 
    updated_at: datetime 
 
    class Config: 
        from_attributes = True 
