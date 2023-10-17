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