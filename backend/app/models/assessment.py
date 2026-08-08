from sqlalchemy import Column, String, Integer, Date, DECIMAL, UUID 
from app.models.base import BaseModel 
import uuid 
 
class Assessment(BaseModel): 
    __tablename__ = "assessments" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    beneficiary_id = Column(UUID(as_uuid=True), nullable=False) 
    program_id = Column(UUID(as_uuid=True), nullable=False) 
    assessment_type = Column(String(20)) 
    date_of_assessment = Column(Date) 
    total_score = Column(DECIMAL(5,2)) 
    obtained_score = Column(DECIMAL(5,2)) 
    percentage = Column(DECIMAL(5,2)) 
    grade = Column(String(5)) 
    assessor_name = Column(String(100)) 
