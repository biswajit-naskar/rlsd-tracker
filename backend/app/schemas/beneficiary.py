from pydantic import BaseModel, Field 
from datetime import date, datetime 
from typing import Optional 
from decimal import Decimal 
from uuid import UUID 
 
class BeneficiaryBase(BaseModel): 
    beneficiary_id: str = Field(..., min_length=3, max_length=50) 
    full_name: str = Field(..., min_length=2, max_length=100) 
    date_of_birth: date 
    gender: str 
    contact_number: Optional[str] = None 
    email: Optional[str] = None 
    village: Optional[str] = None 
    block: Optional[str] = None 
    district: Optional[str] = None 
    state: Optional[str] = "West Bengal" 
    education_level: Optional[str] = None 
    occupation: Optional[str] = None 
    family_income: Optional[Decimal] = None 
 
class BeneficiaryCreate(BeneficiaryBase): 
    pass 
 
class BeneficiaryResponse(BeneficiaryBase): 
    id: UUID 
    is_active: bool 
    created_at: datetime 
    updated_at: datetime 
 
    class Config: 
        from_attributes = True 
