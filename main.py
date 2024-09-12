class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_st(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.lecture_grades:
                lecture.lecture_grades[course] += [grade]
            else:
                lecture.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_value(self):
        if not self.grades:
            return 0
        all_sum = 0
        all_count = 0
        for value_grades_for_one_course in self.grades.values():
            all_sum = all_sum + sum(value_grades_for_one_course)
            all_count = all_count + len(value_grades_for_one_course)
        return all_sum / all_count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.average_value()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')
    def __lt__(self, other):
        return self.average_value() < other.averge_value()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecture_grades = {}

    def average(self):
        if not self.lecture_grades:
            return 0
        all_sum = 0
        all_count = 0
        for value_grades_for_one_course in self.lecture_grades.values():
            all_sum = all_sum + sum(value_grades_for_one_course)
            all_count = all_count + len(value_grades_for_one_course)
        return all_sum / all_count

    def __lt__(self, other):
        return self.average() < other.averge()
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average()}')



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    def rate_rw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman')

some_lecturer.courses_attached += ['Python']

some_student.rate_st(some_lecturer, 'Python', 10)
some_student.rate_st(some_lecturer, 'Python', 10)
some_student.rate_st(some_lecturer, 'Python', 10)

print(some_lecturer)