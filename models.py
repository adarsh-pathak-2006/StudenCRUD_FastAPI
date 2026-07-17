from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Student(Base):
    __tablename__='Student'

    roll_no:Mapped[int] =mapped_column(primary_key=True)
    name:Mapped[str] =mapped_column(String(100))
    age:Mapped[int] =mapped_column(Integer)