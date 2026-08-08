from sqlalchemy import Column, String, Date, Float, Boolean, DECIMAL, Text, Integer 
from sqlalchemy.dialects.postgresql import UUID 
from app.models.base import BaseModel 
import uuid 
 
class Beneficiary(BaseModel): 
    __tablename__ = "beneficiaries" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    beneficiary_id = Column(String(50), unique=True, nullable=False, index=True) 
    full_name = Column(String(100), nullable=False) 
    date_of_birth = Column(Date, nullable=False) 
    gender = Column(String(10), nullable=False) 
    contact_number = Column(String(15)) 
    email = Column(String(100)) 
    village = Column(String(100)) 
    block = Column(String(100)) 
    district = Column(String(100)) 
    state = Column(String(50), default="West Bengal") 
    education_level = Column(String(50)) 
    occupation = Column(String(50)) 
    family_income = Column(DECIMAL(10, 2)) 
    is_active = Column(Boolean, default=True) 
