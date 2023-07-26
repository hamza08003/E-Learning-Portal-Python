from students import Student
from lecturers import Lecturer


class Module:
    valid_departments = ['Computing', 'Science',
                         'Marketing', 'Business', 'Art']

    def __init__(self, module_id, lecturer, module_name="Unknown", course_code="", department="Computing"):
        self.__module_id = self.__validate_module_id(module_id)
        self.__module_name = module_name.strip() or "Unknown"
        self.__course_code = str(course_code).strip()
        self.__department = self.__validate_department(department)
        self.__lecturer = self.__validate_lecturer(lecturer)
        self.__class_list = []
        self.__assessment_list = []

    @staticmethod
    def __validate_module_id(module_id):
        if str(module_id).strip() != "":
            return module_id
        else:
            raise ValueError("Module ID cannot be blank")

    @staticmethod
    def __validate_department(department):
        if department in Module.valid_departments:
            return department
        elif department.strip() == "":
            raise ValueError("Department cannot be blank")
        else:
            raise ValueError("Invalid department")

    @staticmethod
    def __validate_lecturer(lecturer):
        if isinstance(lecturer, Lecturer):
            return lecturer
        else:
            raise ValueError("Invalid lecturer")

    def get_module_id(self):
        return self.__module_id

    def get_module_name(self):
        return self.__module_name

    def set_module_name(self, new_name):
        self.__module_name = new_name.strip() or "Unknown"

    def get_course_code(self):
        return self.__course_code

    def set_course_code(self, new_course_code):
        self.__course_code = str(new_course_code).strip()

    def get_department(self):
        return self.__department

    def set_department(self, new_department):
        self.__department = self.__validate_department(new_department)

    def get_lecturer(self):
        return self.__lecturer

    def set_lecturer(self, new_lecturer):
        self.__lecturer = self.__validate_lecturer(new_lecturer)

    def get_class_list(self):
        return self.__class_list

    def add_student(self, student):
        if isinstance(student, Student) and student not in self.__class_list:
            self.__class_list.append(student)
        else:
            raise ValueError("Invalid student or student already added")

    def remove_student(self, student):
        if isinstance(student, Student) and student in self.__class_list:
            self.__class_list.remove(student)
        else:
            raise ValueError("Invalid student or student not found")

    def get_class_list(self):
        return self.__class_list

    def get_assessment_list(self):
        return self.__assessment_list

    def add_assessment_to_list(self, assessment):
        self.__assessment_list.append(assessment)

    def remove_assessment_from_list(self, assessment):
        self.__assessment_list.remove(assessment)

    def append_to_assessment_list(self, assessment):
        if type(assessment) == list and len(assessment) == 4:
            for items in assessment:
                self.__assessment_list.append(items)
        else:
            raise ValueError("Invalid assessment")

    def __str__(self):
        return f"Module ID: {self.__module_id}\nModule Name: {self.__module_name}\nCourse Code: {self.__course_code}\nDepartment: {self.__department}\nLecturer: {self.__lecturer.get_name()} ({self.__lecturer.get_email_address()})"
