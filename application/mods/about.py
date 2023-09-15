# # # About Me Module
# Handles all pages relative to the about me section
# # #
from app import app
from flask import render_template

# Dictionary to store information about 6 students
students_info = {
    "student1": {
        "name": "Ankita",
        "bio": "This is the bio of Student 1.",
        "email": "amukherjee1@sfsu.edu",
        "photo": "style22.jpg",
    },
    "student2": {
        "name": "Student 2",
        "bio": "This is the bio of Student 2.",
        "email": "student2@example.com",
        "photo": "student2.jpg",
    },
    "student3": {
        "name": "Student 3",
        "bio": "This is the bio of Student 3.",
        "email": "student3@example.com",
        "photo": "student3.jpg",
    },
    "student4": {
        "name": "Student 4",
        "bio": "This is the bio of Student 4.",
        "email": "student4@example.com",
        "photo": "student4.jpg",
    },
    "student5": {
        "name": "Student 5",
        "bio": "This is the bio of Student 5.",
        "email": "student5@example.com",
        "photo": "student5.jpg",
    },
    "student6": {
        "name": "Student 6",
        "bio": "This is the bio of Student 6.",
        "email": "student6@example.com",
        "photo": "student6.jpg",
    },
}
# About me index (list of students)
@app.route("/about")
def about_list():
    return render_template("about_list.html")  # Render the list of students template


# Load template for individual about me pages
@app.route("/about/<string:student>")
def about_page(student):
    if student in students_info:
        return render_template("about_template.html", student=students_info[student])
    else:
        return "Student not found"

def get_about_text():
    # Replace this with your actual about text or logic to retrieve it
    about_text = "Welcome to Team 02's Tutorio! We provide educational content to help you learn and grow."
    return about_text
