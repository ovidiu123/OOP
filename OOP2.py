from enum import Enum
class StudyField(Enum): # STUDY FIELD ENUM
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5
class Student: # STUDENT CLASS
    def __init__(self, first_name, last_name, email, enrolment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolment_date = enrolment_date
        self.date_of_birth = date_of_birth
class Faculty: # FACULTY CLASS
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []

    def assign_student(self, student):
        self.students.append(student)

    def graduate_student(self, email):
        self.students = [s for s in self.students if s.email != email]

    def get_current_students(self):
        return [s for s in self.students]

    def get_graduates(self):
        return [s for s in self.students]

    def has_student(self, email):
        return any(s.email == email for s in self.students)
class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, abbreviation):
        faculty = Faculty(name, abbreviation)
        self.faculties.append(faculty)
        return faculty

    def search_faculty_by_student_email(self, email):
        for faculty in self.faculties:
            if faculty.has_student(email):
                return faculty
        return None

    def display_faculties(self):
        return [faculty.name for faculty in self.faculties]

    def display_faculties_by_field(self, field):
        return [faculty.name for faculty in self.faculties if field.name in faculty.abbreviation]

if __name__ == "__main__":                                     # MAIN PROGRAM LOOP
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
            print("Exiting the program!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break

        else:
            print("Invalid choice.")
