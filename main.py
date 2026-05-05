import student_data

def display_menu():
    print("--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Calculate Average Marks")
    print("4. Exit")
    print("-------------------------------")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            marks_str = input("Enter marks (comma-separated, e.g., 85,90,78): ")
            try:
                marks = [float(m.strip()) for m in marks_str.split(',')]
                success, message = student_data.add_student(name, marks)
                print(message)
            except ValueError:
                print("Invalid marks format. Please enter numbers.")

        elif choice == '2':
            all_students = student_data.get_all_students()
            if not all_students:
                print("No students added yet.")
            else:
                print("--- All Students ---")
                for student in all_students:
                    print(f"Name: {student['name']}, Marks: {student['marks']}")

        elif choice == '3':
            name_to_find = input("Enter student name to calculate average marks: ")
            average = student_data.calculate_average_marks(name_to_find)
            if average is None:
                print(f"Student '{name_to_find}' not found.")
            else:
                print(f"Average marks for {name_to_find}: {average:.2f}")

        elif choice == '4':
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()
