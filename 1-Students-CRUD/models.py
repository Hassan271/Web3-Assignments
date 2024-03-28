from pydantic import BaseModel, Field
from enum import Enum

class Gender(Enum):
    male = "male"
    female = "female"

class Student(BaseModel):
    id: int
    name: str 
    age: int 
    gender: Gender 