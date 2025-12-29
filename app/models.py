from .database import Base
from sqlalchemy import Column, Integer, String,Boolean,DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(Base):
    __tablename__ = "books"
    name = Column(String, primary_key=False,nullable=False)
    author = Column(String, nullable=False)
    rating = Column(Integer,nullable=True)
    year_published = Column(Integer,nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    posted_at = Column(TIMESTAMP (timezone=True), nullable=False, server_default=text('now()'))