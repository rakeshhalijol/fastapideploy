from pydantic import BaseModel

class Student(BaseModel):
    name : str
    rno  : str
    section : str
    marks : list