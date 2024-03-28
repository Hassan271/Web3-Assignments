# Assignment-1 Fast API-----------------------------------------------------------------------------------------
# Hassan Farooq Web-3 PIAIC Quater-3 NTU Roll-NO=PIAIC57456   DATE= 30-Mar-2024 

# Functionality:
#     * Create a global list of students stored in memory.
#         * Implement CRUD operations (Create, Read, Update, Delete) for students:
#         * GET /students: Retrieve all students.
#         * GET /students/{student_id}: Retrieve specific student details.
#         * POST /students: Add a new student.
#         * PUT /students/{student_id}: Update a student's details.
#         * DELETE /students/{student_id}: Delete a student.
# * Student Data Schema:
#         * Each student object should have:
#         * Student ID (unique)
#         * Name
#         * Age
#         * Grade/Class


'use client'


from fastapi import FastAPI, HTTPException, Body
from typing import List
from models import Student, Gender

app = FastAPI()

students = [
    Student(id=1, name="Ali", age=20, gender=Gender.male),
    Student(id=2, name="Bilal", age=21, gender=Gender.male),
    Student(id=3, name="Danish", age=23, gender=Gender.male),
    Student(id=4, name="Esha", age=24, gender=Gender.female),
    Student(id=5, name="Farooq", age=25, gender=Gender.male),
]

@app.get("/")
async def Home():
    return {"Name" : "Ali Raza Galani"}


@app.get("/students")
async def get_students():
    return students

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
async def create_student(student: Student = Body(...)):
    students.append(student)
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student = Body(...)):
    for student_to_update in students:
        if student_to_update.id == student_id:
            student_to_update.name = student.name
            student_to_update.age = student.age
            student_to_update.gender = student.gender
            return student_to_update
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student_to_delete in students:
        if student_to_delete.id == student_id:
            students.remove(student_to_delete)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")