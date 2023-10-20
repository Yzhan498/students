from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data store for students (in-memory storage).
students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = {
        'ID': data['ID'],
        'Name': data['Name'],
        'Grade': data['Grade']
    }
    students.append(new_student)
    return jsonify(new_student), 201
if __name__ == '__main__':
    app.run(debug=True)