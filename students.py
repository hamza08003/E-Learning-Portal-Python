from users import User


class Student(User):
    def __init__(self, email_address, name, department, student_number, programme_code, programme_year, student_type, list_of_grades="None"):
        super().__init__(email_address, name, department)
        self.student_number = self.__validate_student_number(student_number)
        self.programme_code = self.__validate_programme_code(programme_code)
        self.programme_year = self.__validate_programme_year(programme_year)
        self.student_type = self.__validate_student_type(student_type)
        self.list_of_grades = list_of_grades

    @staticmethod
    def __validate_student_number(student_number):
        if isinstance(student_number, int) and len(str(student_number)) == 9:
            return student_number
        else:
            raise ValueError("Invalid student number")

    @staticmethod
    def __validate_programme_code(programme_code):
        if str(programme_code).strip() != "":
            return programme_code
        else:
            raise ValueError("Programme code cannot be blank")

    @staticmethod
    def __validate_programme_year(programme_year):
        valid_years = [1, 2, 3, 4, 5, 6]
        if programme_year in valid_years:
            return programme_year
        else:
            raise ValueError("Invalid programme year")

    @staticmethod
    def __validate_student_type(student_type):
        valid_types = ['fulltime', 'parttime', 'PT', 'FT']
        if student_type in valid_types:
            return student_type
        else:
            raise ValueError("Invalid student type")

    @classmethod
    def auto_add_classlist(cls, file_name, department):
        class_list = []
        with open(file_name, 'r') as f:
            next(f)  # skip the header line
            for line in f:
                fields = line.strip().split(',')
                email_address = fields[0]
                student_name = fields[1]
                student_department = department
                student_number = int(fields[2])
                programme_code = fields[3]
                programme_year = int(fields[4])
                student_type = fields[5]
                list_of_grades = fields[6:] if len(fields) > 6 else None

                student = cls(email_address, student_name, student_department, student_number,
                              programme_code, programme_year, student_type, list_of_grades)
                class_list.append(student)
        return class_list

    @classmethod
    def append_to_class_list(cls, class_list, student):
        class_list.append(student)
        return class_list

    # Getter and Setter for student_number
    def get_student_number(self):
        return self.student_number

    def set_student_number(self, new_student_number):
        self.student_number = self.__validate_student_number(
            new_student_number)

    # Getter and Setter for programme_code
    def get_programme_code(self):
        return self.programme_code

    def set_programme_code(self, new_programme_code):
        self.programme_code = self.__validate_programme_code(
            new_programme_code)

    # Getter and Setter for program_year
    def get_programme_year(self):
        return self.programme_year

    def set_programme_year(self, new_programme_year):
        self.programme_year = self.__validate_programme_year(
            new_programme_year)

    # Getter and Setter for student_type
    def get_student_type(self):
        return self.student_type

    def set_student_type(self, new_student_type):
        self.student_type = self.__validate_student_type(new_student_type)

    # Getter and Setter for grades_list
    def get_list_of_grades(self):
        return self.list_of_grades

    def set_list_of_grades(self, new_list_of_grades):
        self.list_of_grades = new_list_of_grades

    def __str__(self):
        user_info = super().__str__()
        return f"{user_info}\nStudent number: {self.student_number}\nProgramme code: {self.programme_code}\nProgramme year: {self.programme_year}\nStudent type: {self.student_type}\nList of grades: {self.list_of_grades}"
