from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = "Anamika" # default value 
    age : Optional[int] = None  # optional value 
    email : EmailStr
    cgpa: float = Field(gt = 0 , lt = 10, description="A decimal value representing the cgpa of an student") # can apply constraints 

# new_student = {"name" : 20} // Error 

new_student = {'age':32, "email" : "abc@gmail.com", "cgpa": 9}

student = Student(**new_student)
print(student)
