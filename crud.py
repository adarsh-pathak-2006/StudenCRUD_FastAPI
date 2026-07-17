from sqlalchemy.orm import Session
import models
import schema

def create_student(db:Session, student:schema.StudentCreate):
    db_student=models.Student(roll_no=student.roll_no, name=student.name, age=student.age)