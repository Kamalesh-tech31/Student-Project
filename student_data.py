# Global list to store student data
students = []

def add_student(name, marks):
    """Adds a new student with their marks to the global list."""
    if not isinstance(name, str) or not name:# checks if name is string
        return False, "Invalid name provided."
    if not isinstance(marks, list) or not all(isinstance(m, (int, float)) for m in marks):#checks if marks is list
        return False, "Invalid marks list provided."
    
    student_record = {
        'name': name,
        'marks': marks
    }
    students.append(student_record)
    return True, "Student added successfully."

def get_all_students():
    """Returns the list of all students."""
    return students

def calculate_average_marks(student_name):
    """Calculates the average marks for a specific student."""
    for student in students:
        if student['name'] == student_name:
            if not student['marks']:
                return 0  # Return 0 if no marks are present
            return sum(student['marks']) / len(student['marks'])
    return None # Student not found

def get_student_by_name(name):
    """Finds and returns a student record by name."""
    for student in students:
        if student['name'] == name:
            return student
    return None