from sqlalchemy import Column, String, Integer, Date, Text, Boolean, UUID 
from app.models.base import BaseModel 
import uuid 
 
class Feedback(BaseModel): 
    __tablename__ = "feedback" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    beneficiary_id = Column(UUID(as_uuid=True), nullable=False) 
    program_id = Column(UUID(as_uuid=True), nullable=False) 
    feedback_date = Column(Date, nullable=False) 
    satisfaction_score = Column(Integer, nullable=False) 
    training_quality = Column(Integer, nullable=False) 
    comments = Column(Text) 
    suggestions = Column(Text) 
    follow_up_required = Column(Boolean, default=False) 
