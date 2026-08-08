from pydantic import BaseModel 
from datetime import date, datetime 
from typing import Optional 
from uuid import UUID 
from decimal import Decimal 
 
class AssessmentBase(BaseModel): 
    beneficiary_id: UUID 
    program_id: UUID 
    assessment_type: str 
    date_of_assessment: date 
    total_score: Decimal 
    obtained_score: Decimal 
    assessor_name: Optional[str] = None 
 
class AssessmentCreate(AssessmentBase): 
    pass 
 
class AssessmentResponse(AssessmentBase): 
    id: UUID 
    percentage: Optional[Decimal] = None 
    grade: Optional[str] = None 
    created_at: datetime 
    updated_at: datetime 
 
    class Config: 
        from_attributes = True 
