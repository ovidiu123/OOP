from student_faculty import Faculty
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
