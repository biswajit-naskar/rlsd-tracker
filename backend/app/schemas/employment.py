from pydantic import BaseModel 
from datetime import date, datetime 
from typing import Optional 
from uuid import UUID 
from decimal import Decimal 
 
class EmploymentBase(BaseModel): 
    beneficiary_id: UUID 
    program_id: UUID 
    employment_status: str 
    job_title: Optional[str] = None 
    employer_name: Optional[str] = None 
    monthly_income: Optional[Decimal] = None 
    employment_date: Optional[date] = None 
    is_sustainable: bool = False 
    follow_up_date: Optional[date] = None 
    notes: Optional[str] = None 
 
class EmploymentCreate(EmploymentBase): 
    pass 
 
class EmploymentResponse(EmploymentBase): 
    id: UUID 
    created_at: datetime 
    updated_at: datetime 
 
    class Config: 
        from_attributes = True 
