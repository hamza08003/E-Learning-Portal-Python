import random


class GradeCalculator:
    @staticmethod
    def percentage_to_grade(percentage):
        if 80 <= percentage <= 100:
            return "A"
        elif 70 <= percentage < 80:
            return "B+"
        elif 60 <= percentage < 70:
            return "B"
        elif 55 <= percentage < 60:
            return "B-"
        elif 50 <= percentage < 55:
            return "C+"
        elif 40 <= percentage < 50:
            return "C"
        elif 35 <= percentage < 40:
            return "D"
        elif percentage < 35:
            return "F"
        else:
            raise ValueError("Invalid percentage value")

    @staticmethod
    def grade_to_percentage(grade):
        if grade == "A":
            return random.randint(80, 100)
        elif grade == "B+":
            return random.randint(70, 79)
        elif grade == "B":
            return random.randint(60, 69)
        elif grade == "B-":
            return random.randint(55, 59)
        elif grade == "C+":
            return random.randint(50, 54)
        elif grade == "C":
            return random.randint(40, 49)
        elif grade == "D":
            return random.randint(35, 39)
        elif grade == "F":
            return random.randint(0, 34)
        else:
            raise ValueError("Invalid grade value")
