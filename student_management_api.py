from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample student data
students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "John",
        "age": 21,
        "branch": "Mechanical"
    },
    {
        "id": 3,
        "name": "Arun",
        "age": 22,
        "branch": "Computer Science"
    },
    {
        "id": 4,
        "name": "Anu",
        "age": 20,
        "branch": "Electrical"
    },
    {
        "id": 5,
        "name": "Niya",
        "age": 21,
        "branch": "Computer Science"
    }
]

# Home Route
@app.route('/')
def home():
    return "Welcome to My First Flask Application"


# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# Update Student
@app.route('/update-student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student["id"] == id:

            if "name" in data:
                student["name"] = data["name"]

            if "age" in data:
                student["age"] = data["age"]

            if "branch" in data:
                student["branch"] = data["branch"]

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            })

    return jsonify({"error": "Student not found"}), 404


# Student Count
@app.route('/student-count', methods=['GET'])
def student_count():
    return jsonify({
        "total_students": len(students)
    })


# Student Branch Filter
@app.route('/students/branch/<branch>', methods=['GET'])
def students_by_branch(branch):

    filtered_students = []

    for student in students:
        if student["branch"].lower() == branch.lower():
            filtered_students.append(student)

    return jsonify(filtered_students)


if __name__ == '__main__':
    app.run(debug=True)
    