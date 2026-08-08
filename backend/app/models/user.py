from sqlalchemy import Column, String, Boolean, UUID 
from app.models.base import BaseModel 
import uuid 
 
class User(BaseModel): 
    __tablename__ = "users" 
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    username = Column(String(50), unique=True, nullable=False, index=True) 
    email = Column(String(100), unique=True, nullable=False) 
    hashed_password = Column(String(255), nullable=False) 
    is_active = Column(Boolean, default=True) 
    full_name = Column(String(100)) 
