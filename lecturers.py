from users import User


class Lecturer(User):
    __num_lectures = 0

    def __init__(self, email, name, department, staff_id, speciality, qualification):
        super().__init__(email, name, department)
        self.staff_id = self.__validate_lecturer_id(staff_id)
        self.speciality = speciality
        qualification = qualification.upper()
        if qualification not in ['BA', 'BSC', 'MA', 'MSC', 'PHD']:
            raise ValueError("Invalid qualification")
        self.qualification = qualification
        Lecturer.__num_lectures += 1

    @staticmethod
    def __validate_lecturer_id(staff_id):
        staff_id_str = str(staff_id)
        if not staff_id_str.isnumeric():
            raise ValueError("Staff ID must contain only numeric characters")
        if len(staff_id_str) != 6:
            raise ValueError("Staff ID must be 6 digits in length")
        return staff_id_str

    @classmethod
    def get_num_lectures(cls):
        return cls.__num_lectures

    @classmethod
    def set_num_lectures(cls, num_lectures):
        cls.__num_lectures = num_lectures

    # Getter lecturer name
    def get_lecturer_name(self):
        return self.name

    # Getter and setter for staff_id
    def get_staff_id(self):
        return self.staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = self.__validate_lecturer_id(staff_id)

    # Getter and setter for speciality
    def get_speciality(self):
        return self.speciality

    def set_speciality(self, speciality):
        self.speciality = speciality

    # Getter and setter for qualification
    def get_qualification(self):
        return self.qualification

    def set_qualification(self, qualification):
        qualification = qualification.upper()
        if qualification not in ['BA', 'BSC', 'MA', 'MSC', 'PHD']:
            raise ValueError("Invalid qualification")
        self.qualification = qualification

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email_address}\nDepartment: {self.department}\n" \
               f"Staff ID: {self.staff_id}\nSpeciality: {self.speciality}\nQualification: {self.qualification}"
