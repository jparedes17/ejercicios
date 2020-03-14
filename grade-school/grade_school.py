from typing import List


class School:
    def __init__(self):
        self.students: List[[int, str]] = []

    def add_student(self, name: str, grade: int):
        self.students.append([grade, name])

    def roster(self) -> List[str]:
        self.students.sort()
        return [i[1] for i in self.students]

    def grade(self, grade_number) -> List[str]:
        self.students.sort()
        return [i[1] for i in self.students if i[0] == grade_number]