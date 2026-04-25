from .database import Base
from sqlalchemy import Column, Integer, String,Boolean,DateTime, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(Base):
    __tablename__ = "books"
    name = Column(String, primary_key=False,nullable=False)
    author = Column(String, nullable=False)
    rating = Column(Integer,nullable=True)
    year_published = Column(Integer,nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    posted_at = Column(TIMESTAMP (timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    owner = relationship("Users")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('now()')
    )
    phone = Column(String, nullable=False)

class Votes(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key=True)
    

