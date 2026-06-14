"""
Task: Student Grade Manager.

A simple console-based application to manage student records and grades.

This program allows users to:
- Add new students with name, ID, and marks
- View all student records
- Calculate grades based on marks
- Display class summary (average, highest, lowest marks)

This project demonstrates:
- Python functions
- Data structures (lists)
- Dataclasses
- Conditional logic
- Menu-driven program design
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


# Import library
from dataclasses import dataclass


@dataclass
class Student:
    name: str # Student Name
    student_id: str # Student ID
    mark: float # Student's mark
    

students : list[Student] = []


def calculate_grade(mark: float) -> str:
    """
    Calculates grade based on student mark.

    Args:
        mark: float  # Student's numeric mark

    Returns:
           str  # Grade (HD, DN, CR, PP, NN)
    """

    if mark >= 80:
        return "HD"

    elif mark >=70:
        return "DN"

    elif mark >= 60:
        return "CR"
    
    elif mark >= 50:
        return "PP"

    else:
        return "NN"


def add_student(name: str, student_id: str, mark: float):
    """
    Adds a new student ID.

    Args:
        name: str  # Student Name
        student_id: str  # Unique Student ID
        mark: float  # Student's mark

    Returns: None
    """

    for student in students:
        if student.name.lower() == name.lower():
            print("Student already exixts.")
            return

    student = Student(name, student_id, mark )
    students.append(student)

    print("Student added successfully!")


def view_students():
    """
    Displays all students.

    Args: None
    Returns: None
    """

    if not students:
        print("No student found.")
        return

    for student in students:
        
        grade = calculate_grade(student.mark)

        print(f"Name: {student.name}")
        print(f"Student ID: {student.student_id}")
        print(f"Mark: {student.mark}")
        print(f"Grade: {grade}")
        

def class_summary():
    """
    Displays summary statistics of the class.

    Args: None
    Returns: None
    """

    if not students:
        print("No data found.")
        return
    
    marks = []

    for student in students:
        marks.append(student.mark)

    print("-----Class Summary-----")
    print(f"\nTotal students: {len(students)}")
    print(f"Average Mark: {sum(marks) / len(marks):.2f}")
    print(f"Highest Mark: {max(marks)}")
    print(f"Lowest Mark: {min(marks)}")


def main():
    """
    Main menu-driven program loop.
    """

    while True:
        
        print("\n=====Grade Manager App=====")
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Class Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                name = input("Enter name: ")
                student_id = input("Enter ID: ")
                mark = float(input("Enter mark: "))
                add_student(name, student_id, mark)

            case "2":
                view_students()

            case "3":
                class_summary()

            case "4":
                print("Good Bye!")
                break

            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main()
       






























































