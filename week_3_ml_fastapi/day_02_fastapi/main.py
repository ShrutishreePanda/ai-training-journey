###Student Management API


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI(title="Student Management API")

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added",
        "student": student
    }

@app.get("/students", response_model=List[Student])
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):

    for index, student in enumerate(students):

        if student.id == student_id:
            students[index] = updated_student
            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:
            students.pop(index)

            return {
                "message": "Deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )