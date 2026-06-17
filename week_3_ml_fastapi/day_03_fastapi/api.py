# Nested Models
# Validators
# File Upload
# Headers
# Forms
# Cookies

from fastapi import FastAPI, UploadFile, File, Header, Form
from pydantic import BaseModel, EmailStr, field_validator

app = FastAPI(title="Employee Portal")

class Address(BaseModel):
    city: str
    state: str

class Employee(BaseModel):
    name: str
    email: EmailStr
    age: int
    address: Address

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):

        if value < 18:
            raise ValueError(
                "Employee must be 18+"
            )

        return value

employees = []

@app.post("/employees")
def add_employee(employee: Employee):

    employees.append(employee)

    return {
        "message": "Employee added"
    }

@app.get("/employees")
def get_employees():
    return employees

@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    content = await file.read()

    return {
        "filename": file.filename,
        "size": len(content)
    }

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    return {
        "username": username
    }

@app.get("/headers")
def read_header(
    user_agent: str = Header(...)
):

    return {
        "user_agent": user_agent
    }