from sqlalchemy import Column, String, Date, Boolean, DECIMAL, Text, UUID 
from app.models.base import BaseModel 
import uuid 
 
class Employment(BaseModel): 
    __tablename__ = "employment_tracking" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    beneficiary_id = Column(UUID(as_uuid=True), nullable=False) 
    program_id = Column(UUID(as_uuid=True), nullable=False) 
    employment_status = Column(String(30), nullable=False) 
    job_title = Column(String(100)) 
    employer_name = Column(String(100)) 
    monthly_income = Column(DECIMAL(10, 2)) 
    employment_date = Column(Date) 
    is_sustainable = Column(Boolean, default=False) 
    follow_up_date = Column(Date) 
    notes = Column(Text) 
