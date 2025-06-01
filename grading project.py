import os

# Function to calculate the average of grades for each student
def calculate_average(grades):
    return sum(grades.values()) / len(grades)

# Function to assign a letter grade based on the average
def assign_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Function to load student data from a file
def load_students(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            students = []
            for line in file:
                name, grades_str = line.strip().split(":")
                grades = eval(grades_str)  # Convert string representation of dict back to dictionary
                students.append((name, grades))
            return students
    return []

# Function to save student data to a file
def save_students(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            name, grades = student
            file.write(f"{name}:{grades}\n")

# Function to display the grades of a student
def display_student_grades(student):
    name, grades = student
    average = calculate_average(grades)
    letter_grade = assign_letter_grade(average)
    print(f"\nName: {name}")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")

# Main function to manage the student grades system
def main():
    filename = 'students.txt'
    students = load_students(filename)
    
    while True:
        print("\nStudent Grading System Menu:")
        print("1. Add New Student")
        print("2. View Student Grades")
        print("3. Modify Student Grades")
        print("4. View All Students")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Add New Student
            name = input("Enter the student's name: ")
            grades = {}
            while True:
                subject = input("Enter subject name (or type 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                grades[subject] = grade
            students.append((name, grades))
        
        elif choice == '2':  # View Specific Student's Grades
            name = input("Enter the student's name: ")
            student_found = False
            for student in students:
                if student[0].lower() == name.lower():
                    display_student_grades(student)
                    student_found = True
                    break
            if not student_found:
                print("Student not found!")

        elif choice == '3':  # Modify Student Grades
            name = input("Enter the student's name: ")
            student_found = False
            for i, student in enumerate(students):
                if student[0].lower() == name.lower():
                    print("Current grades:", student[1])
                    subject = input("Enter the subject to modify: ")
                    if subject in student[1]:
                        new_grade = float(input(f"Enter the new grade for {subject}: "))
                        student[1][subject] = new_grade
                        print(f"Grade for {subject} updated.")
                    else:
                        print(f"{subject} not found!")
                    students[i] = student  # Update the student data
                    student_found = True
                    break
            if not student_found:
                print("Student not found!")

        elif choice == '4':  # View All Students' Grades
            if not students:
                print("No students available.")
            else:
                for student in students:
                    display_student_grades(student)

        elif choice == '5':  # Save and Exit
            save_students(students, filename)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main() 