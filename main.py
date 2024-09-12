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

student_1 = Student('koy', 'fit')
student_2 = Student('filip', 'stoun')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['C+']
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Java']
student_list = [student_1 , student_2]

lecturer_1 = Lecturer('play', 'boy')
lecturer_2 = Lecturer('guy', 'women')
rewiewer_1 = Reviewer('do', 'work')
rewiewer_2 = Reviewer('play', 'man')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
rewiewer_1.courses_attached += ['Python']
rewiewer_1.courses_attached += ['Java']
lecturer_2.courses_attached += ['Python']
rewiewer_2.courses_attached += ['Java']
lecture_list = [lecturer_1 , lecturer_2]

rewiewer_1.rate_rw(student_1, 'Python', 10)
rewiewer_1.rate_rw(student_1, 'Java', 9)
rewiewer_2.rate_rw(student_1, 'Java', 9)
rewiewer_1.rate_rw(student_2, 'Python', 9)
rewiewer_1.rate_rw(student_2, 'Python', 9)
rewiewer_1.rate_rw(student_2, 'Python', 9)
rewiewer_1.rate_rw(student_2, 'Python', 10)

student_1.rate_st(lecturer_1, 'Java', 10)
student_2.rate_st(lecturer_1, 'Java', 8)
student_1.rate_st(lecturer_1, 'Python', 8)
student_2.rate_st(lecturer_1, 'Python', 8)
student_1.rate_st(lecturer_2, 'Python', 9)
student_2.rate_st(lecturer_2, 'Python', 8)

def grades_student(student_list, course):
    for student in student_list:
        for grades in student.grades:
            grades_list = student.grades.get(course)
            all_grades = sum(grades_list)
            len_grades = len(grades_list)
            return all_grades / len_grades

def grades_lecturer(lecture_list, course):
    for lecture in lecture_list:
        for grades in lecture.lecture_grades:
            grades_list1 = lecture.lecture_grades.get(course)
            all_grades1 = sum(grades_list1)
            len_grades1 = len(grades_list1)
            return all_grades1 / len_grades1

print (student_1)
print (lecturer_1)
print (student_1.average_value() < student_2.average_value())
print (student_1.average_value() == student_2.average_value())
print (lecturer_1.average() == lecturer_2.average())
print (grades_lecturer(lecture_list, 'Python'))
print (grades_student(student_list, 'Java'))

