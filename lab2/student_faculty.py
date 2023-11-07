class Student:
    def __init__(self, first_name, last_name, email, enrolment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolment_date = enrolment_date
        self.date_of_birth = date_of_birth

class Faculty:
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
