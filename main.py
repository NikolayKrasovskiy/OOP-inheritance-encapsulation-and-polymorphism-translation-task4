class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_average_grade
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за домашние задания: {avg_grade:.1f} '
                f'Курсы в процессе изучения: {courses_in_progress} '
                f'Завершенные курсы: {finished_courses}')

    @property
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

    def __lt__(self, other):
        return self.get_average_grade < other.get_average_grade

    def __le__(self, other):
        return self.get_average_grade <= other.get_average_grade

    def __gt__(self, other):
        return self.get_average_grade > other.get_average_grade

    def __ge__(self, other):
        return self.get_average_grade >= other.get_average_grade

    def __eq__(self, other):
        return self.get_average_grade == other.get_average_grade

    def __ne__(self, other):
        return self.get_average_grade != other.get_average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_average_grade
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    @property
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_lecturer(self, lecturer, course, grade):
        if course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print(f'Cannot rate {lecturer.name} {lecturer.surname}, lecturer does not teach this course.')

    def rate_student(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f'Review cannot be made, {student.name} is not enrolled in {course}.')


# Functions for calculating averages

def average_student_grade(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grades / count if count > 0 else 0


def average_lecturer_grade(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grades / count if count > 0 else 0


# Creating objects
best_student1 = Student('Ruoy', 'Eman', 'Male')
best_student1.finished_courses += ['Git']
best_student1.courses_in_progress += ['Python']
best_student1.grades['Git'] = [10, 10, 10, 10, 10]
best_student1.grades['Python'] = [10, 10]

best_student2 = Student('John', 'Smith', 'Male')
best_student2.finished_courses += ['Git']
best_student2.courses_in_progress += ['Python', 'Java']
best_student2.grades['Git'] = [9, 8, 10, 10, 9]
best_student2.grades['Python'] = [9, 8]

cool_lecturer1 = Lecturer('John', 'Doe')
cool_lecturer1.courses_attached += ['Python']
cool_lecturer1.grades['Python'] = [8, 9, 10]

cool_lecturer2 = Lecturer('Jane', 'Roe')
cool_lecturer2.courses_attached += ['Python', 'Java']
cool_lecturer2.grades['Python'] = [10, 9, 10]
cool_lecturer2.grades['Java'] = [9, 10]

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']

# Rating students and lecturers
cool_reviewer.rate_student(best_student1, 'Python', 9)
cool_reviewer.rate_student(best_student2, 'Python', 8)
cool_reviewer.rate_lecturer(cool_lecturer1, 'Python', 9)
cool_reviewer.rate_lecturer(cool_lecturer2, 'Python', 10)

# Output information
print(cool_reviewer)
print(cool_lecturer1)
print(cool_lecturer2)
print(best_student1)
print(best_student2)

# Examples of comparisons
print(best_student1 > cool_lecturer1)  # Comparison between student and lecturer