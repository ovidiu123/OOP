from study_field import StudyField
from student import Student
from faculty import Faculty
from university import University

if __name__ == "__main__":
    print("WELCOME TO TUM'S STUDENT MANAGEMENT SYSTEM!")

    university = University()

    while True:

        print("\nChoose an option:")
        print("1 - General options")
        print("2 - Faculty operations")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nGENERAL OPTIONS:")
                print("1 - Create Faculty")
                print("2 - Display University Faculties")
                print("3 - Search Student and Show Faculty")
                print("4 - Display All Faculties of a Field")
                print("5 - Go back")

                general_choice = input("Enter your choice: ")

                if general_choice == "1":
                    name = input("Enter faculty name: ")
                    abbreviation = input("Enter faculty abbreviation: ")
                    university.create_faculty(name, abbreviation)
                    print("Faculty created successfully!")

                elif general_choice == "2":
                    faculties = university.display_faculties()
                    print("University Faculties:")
                    for faculty in faculties:
                        print(faculty)

                elif general_choice == "3":
                    email = input("Enter student email: ")
                    faculty = university.search_faculty_by_student_email(email)
                    if faculty:
                        print(f"Student with email '{email}' belongs to '{faculty.name}' Faculty.")
                    else:
                        print(f"Student with email '{email}' not found in any faculty.")

                elif general_choice == "4":
                    field = input("Enter a field (e.g., FOOD_TECHNOLOGY): ")
                    field_enum = StudyField[field]
                    faculties = university.display_faculties_by_field(field_enum)
                    print(f"Faculties related to {field_enum.name}:")
                    for faculty in faculties:
                        print(faculty)

                elif general_choice == "5":
                    break  # Go back to the main menu

                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "2":
            while True:
                print("\nFACULTY OPERATIONS:")
                print("1 - Create Student")
                print("2 - Graduate Student")
                print("3 - Display Enrolled Students")
                print("4 - Display Graduated Students")
                print("5 - Check if Student Belongs to a Faculty")
                print("6 - Go back")

                faculty_choice = input("Enter your choice: ")

                if faculty_choice == "1":
                    first_name = input("Enter student's first name: ")
                    last_name = input("Enter student's last name: ")
                    email = input("Enter student's email: ")
                    enrolment_date = input("Enter enrolment date (YYYY-MM-DD): ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    student = Student(first_name, last_name, email, enrolment_date, date_of_birth)

                    print("Faculties available for enrollment:")
                    for i, faculty in enumerate(university.faculties):
                        print(f"{i + 1} - {faculty.name}")

                    faculty_index = int(input("Select a faculty (1, 2, etc.): ")) - 1

                    if 0 <= faculty_index < len(university.faculties):
                        faculty = university.faculties[faculty_index]
                        faculty.assign_student(student)
                        print(f"Student {student.first_name} {student.last_name} enrolled in {faculty.name}.")

                elif faculty_choice == "2":
                    email = input("Enter student's email to graduate: ")
                    faculty = university.search_faculty_by_student_email(email)
                    if faculty:
                        faculty.graduate_student(email)
                        print(f"Student with email '{email}' graduated from '{faculty.name}' Faculty.")
                    else:
                        print(f"Student with email '{email}' not found in any faculty.")

                elif faculty_choice == "3":
                    print("Faculties available for displaying enrolled students:")
                    for i, faculty in enumerate(university.faculties):
                        print(f"{i + 1} - {faculty.name}")

                    faculty_index = int(input("Select a faculty (1, 2, etc.): ")) - 1

                    if 0 <= faculty_index < len(university.faculties):
                        faculty = university.faculties[faculty_index]
                        current_students = faculty.get_current_students()
                        print(f"Enrolled Students in {faculty.name}:")
                        for student in current_students:
                            print(f"{student.first_name} {student.last_name} ({student.email})")

                elif faculty_choice == "4":
                    print("Faculties available for displaying graduated students:")
                    for i, faculty in enumerate(university.faculties):
                        print(f"{i + 1} - {faculty.name}")

                    faculty_index = int(input("Select a faculty (1, 2, etc.): ")) - 1

                    if 0 <= faculty_index < len(university.faculties):
                        faculty = university.faculties[faculty_index]
                        graduates = faculty.get_graduates()
                        print(f"Graduated Students from {faculty.name}:")
                        for student in graduates:
                            print(f"{student.first_name} {student.last_name} ({student.email})")

                elif faculty_choice == "5":
                    faculty_abbreviation = input("Enter faculty abbreviation: ")
                    email = input("Enter student email: ")
                    faculty = university.faculties[faculty_index]
                    if faculty.has_student(email):
                        print(f"Student with email '{email}' belongs to '{faculty.name}' Faculty.")
                    else:
                        print(f"Student with email '{email}' not found in '{faculty.name}' Faculty.")

                elif faculty_choice == "6":
                    break    # GO BACK TO MAIN MENU

                else:
                    print("Invalid choice.")

        elif choice == "3":
            print("Exiting the program!!!!!!!!!")
            break

        else:
            print("Invalid choice.")