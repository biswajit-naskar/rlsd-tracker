from sqlalchemy import Column, String, Integer, Date, Text, UUID 
from app.models.base import BaseModel 
import uuid 
 
class TrainingProgram(BaseModel): 
    __tablename__ = "training_programs" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    program_code = Column(String(20), unique=True, nullable=False) 
    program_name = Column(String(100), nullable=False) 
    category = Column(String(50)) 
    description = Column(Text) 
    duration_days = Column(Integer) 
    start_date = Column(Date) 
    end_date = Column(Date) 
    status = Column(String(20), default="Planned") 
