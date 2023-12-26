import datetime
from pydantic import BaseModel, validator
from typing import List, Optional


class SummaryCreateIn(BaseModel):  #입력스키마
    content: str                   #입력contents
    mode:  Optional[str] = None    #요청mode

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    class Config:
        orm_mode = True

class SummaryCreateOut(BaseModel):  #출력스키마
    content: str
    create_date: datetime.datetime
    
    class Config:
        orm_mode = True

class SummaryCreate(BaseModel):  
    content: str
    summary: str
    create_date: Optional[datetime.datetime]

    class Config:
        orm_mode = True

class Summary(BaseModel):  #미 사용 스키마임
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True