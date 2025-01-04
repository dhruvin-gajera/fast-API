from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer,primary_key = True,index= True)
    question_txt = Column(String,index= True)

class Choices(Base):
    __tablename__ = "choices"

    id = Column(Integer,primary_key = True,index=True)
    choice_txt = Column(String,index=True)
    is_correct = Column(Boolean,default=False)
    question_id = Column(Integer,ForeignKey("question.id"))