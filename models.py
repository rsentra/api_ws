# alembic을 사용하지 않고 스키마를 생성함: python models.py를 실행하면 생성됨
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import engine
from database import Base

class Chat_content(Base):
    __tablename__ = "chat_content"
    __table_args__ = {'schema': 'ai_chat'}   # postgresql schema지정

    id = Column(Integer, primary_key=True)
    content_source = Column(Text, nullable=False)
    content_summary = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)


#--cmd창에서 파이썬으로 아래 실행해보자
# python
# from models import Chat_content
# from datetime import datetime
# q = Chat_content(content_source='채팅 대화내용컬럼입니다.', content_summary ='채팅 요약 컬럼입니다.', create_date=datetime.now())
# from database import SessionLocal
# db = SessionLocal()
# db.add(q)
# db.commit()

