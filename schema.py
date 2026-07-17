from pydantic import BaseModel

class StudentCreate(BaseModel):
    roll_no:int
    name:str
    age:int

class StudentUpdate(BaseModel):
    name:str
    age:int

class StudentResponse(BaseModel):
    roll_no:int
    name:str
    age:int

    model_config={"from_attributes":True}