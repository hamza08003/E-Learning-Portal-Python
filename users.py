import re
import random
import datetime as dt


class User:
    __user_count = 0

    def __init__(self, email_address, name, department):
        self.email_address = self.__validate_email(email_address)
        self.password = self.__generate_password()
        self.name = self.__validate_name(name)
        self.department = self.__validate_department(department)
        self.date_registered = dt.date.today()
        User.__user_count += 1

    @staticmethod
    def __validate_email(email_address):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_address) and email_address.endswith('.com'):
            return email_address
        else:
            raise ValueError("Invalid email address format")

    @staticmethod
    def __generate_password():
        return str(random.randint(0, 10000))

    @staticmethod
    def __validate_name(name):
        if name.strip() != "":
            return name
        else:
            raise ValueError("Name cannot be blank")

    @staticmethod
    def __validate_department(department):
        valid_departments = ['Computing', 'Science',
                             'Marketing', 'Business', 'Art']
        if department in valid_departments:
            return department
        elif department.strip() == "":
            raise ValueError("Department cannot be blank")
        else:
            raise ValueError("Invalid department")

    # Getter Method for User Count
    @classmethod
    def get_user_count(cls):
        return cls.__get_user_count()

    # Setter Method for User Count
    @classmethod
    def set_user_count(cls, count):
        cls.__set_user_count(count)
        print(f"User Count set to {count}")

    # Getter method for email_address
    def get_email_address(self):
        return self.email_address

    # Setter method for email_address
    def set_email_address(self, new_email_address):
        self.email_address = self.__validate_email(new_email_address)

    # Getter method for password
    def get_password(self):
        return self.password

    # Setter method for password
    def set_password(self, new_password):
        self.password = new_password

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, new_name):
        self.name = self.__validate_name(new_name)

    # Getter method for department
    def get_department(self):
        return self.department

    # Setter method for department
    def set_department(self, new_department):
        self.department = self.__validate_department(new_department)

    # Getter method for date_registered
    def get_date_registered(self):
        return self.date_registered

    # Setter method for date_registered
    def set_date_registered(self, new_registration_date):
        self.date_registered = new_registration_date

    def __str__(self):
        return f"Email address: {self.email_address}\nPassword: {self.password}\nName: {self.name}\nDepartment: {self.department}\nDate registered: {self.date_registered}"
