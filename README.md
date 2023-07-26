# E-Learning-Portal-Python
🐍 This repository contains the source code for a Terminal-Based E-Learning Portal implemented in Python. The project aims to create a MOOC platform similar to Moodle, featuring User, Student, Lecturer, and Module classes, along with a GradeCalculator utility for student assessments.

# Features:
User Class: A class representing users of the e-learning platform, with attributes like email address, password, name, department, and registration date. 👤

Student Class: A subclass of the User class, specifically for representing students. It includes attributes like student number, program code, program year, student type, and a list of grades. 🎓

Lecturer Class: Another subclass of the User class, for representing lecturers. It contains attributes like staff ID, specialty, and qualification. 👨‍🏫

Module Class: A class to represent individual class modules in the e-learning portal. It includes attributes like Module ID, Module Name, Course Code, Department, Lecturer, Student Class List, and Assessment List. 📚

GradeCalculator Utility Class: A static utility class with a method for converting percentages to grades for student assessments. 📊

# 🖥️ Main Program:
The main program allows users to interact with the E-Learning Portal. It offers the following functionalities through a menu:

1) Add Module: Users can add new modules to the system. ➕

2) Add Students to Module: Users can add students to specific modules, either manually or by reading from a file (e.g., Students.csv). 📝

3) Add Student Grades to Module: Users can enter assessment details for students, and the GradeCalculator will convert the percentages to grades. 📈

4) Display List of Modules: Users can view the list of all modules and get statistics, such as the total number of modules and the number of modules by department. 📋

5) Display List of Students: Users can view all students in a particular module and get the total number of students in that module. 👥

6) Display List of Students Grades: Users can view the grade information for a specific module and get the number of students in each grade category. 📜

7) Exit: Before exiting the program, the updated list of modules is saved to Modules.csv. 🔄

# ℹ️ How to Use:
Clone the repository to your local machine. 📥
Run the main program (e.g., main.py) to access the E-Learning Portal functionalities. 🏃‍♂️
Follow the on-screen instructions to perform various tasks in the portal. 📝
Feel free to contribute, report issues, or suggest improvements to make this E-Learning Portal even better! Happy learning! 😊
Let's make learning fun and accessible for everyone! 🌟
