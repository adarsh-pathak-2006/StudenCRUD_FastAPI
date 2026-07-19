from sqlalchemy.orm import Session
import models
import schema

def create_student(db:Session, student:schema.StudentCreate):
    db_student=models.Student(roll_no=student.roll_no, name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db:Session):
    db.query(models.Student).all()

def get_student(db:Session, roll_no:int):
   obj=db.query(models.Student).filter(models.Student.roll_no==roll_no).first()
   return obj

def update_student(db:Session, roll_no:int, studen=schema.StudentUpdate):
    student_data=get_student(db, roll_no)
    if student_data is None:
        return None
    else:
        student_data.name=studen.name
        student_data.age=studen.age

        db.commit()
        db.refresh(student_data)
        return student_data
    

def delete_student(db:Session, roll_no:int):
    db_student=get_student(db, roll_no)
    if db_student is None:
        return None
    else:
        db.delete(db_student)
        db.commit()
        db.refresh(db_student)
        