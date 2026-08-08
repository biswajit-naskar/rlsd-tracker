from pydantic import BaseModel 
from datetime import date, datetime 
from typing import Optional 
from uuid import UUID 
 
class ProgramBase(BaseModel): 
    program_code: str 
    program_name: str 
    category: Optional[str] = None 
    description: Optional[str] = None 
    duration_days: Optional[int] = None 
    start_date: Optional[date] = None 
    end_date: Optional[date] = None 
    status: Optional[str] = "Planned" 
 
class ProgramCreate(ProgramBase): 
    pass 
 
class ProgramResponse(ProgramBase): 
    id: UUID 
    created_at: datetime 
    updated_at: datetime 
 
    class Config: 
        from_attributes = True 
