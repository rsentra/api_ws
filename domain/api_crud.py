from models import Chat_content
from sqlalchemy.orm import Session
from domain.api_schema import SummaryCreate
from datetime import datetime

def create_content(db: Session, content_create: SummaryCreate):
    db_content = Chat_content(content_source = content_create.content,
                              content_summary = content_create.summary,
                               create_date = content_create.create_date)
                            #   create_date = datetime.now())
    db.add(db_content)
    db.commit()