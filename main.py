import csv
from students import Student
from lecturers import Lecturer
from grades_calc import GradeCalculator
from modules import Module


def main():

    # Create an empty list to store the modules
    module_list = []

    # Open the CSV file
    with open('modules.csv', 'r') as modules_list_file:
        # Create a CSV reader object
        reader = csv.reader(modules_list_file)

        # Skip the header row
        next(reader)

        # Loop over the rows in the CSV file
        for row in reader:
            # Extract the fields from the row
            module_id = row[0]
            module_name = row[1]
            course_code = row[2]
            department = row[3]
            lecturer_email = row[4]
            lecturer_name = row[5]
            lecturer_staff_id = row[6]
            lecturer_speciality = row[7]
            lecturer_qualification = row[8]

            # Create a new Lecturer object
            lecturer = Lecturer(lecturer_email, lecturer_name, department,
                                lecturer_staff_id, lecturer_speciality, lecturer_qualification)

            # Create a new Module object and add it to the list
            module = Module(module_id, lecturer, module_name,
                            course_code, department)
            module_list.append(module)

    # fucntion to add new module to the system

    def add_module():
        module_id = input("Enter Module ID: ")
        for module_IDs in module_list:
            if module_IDs.get_module_id() == module_id:
                print("Module Id already exists")
                return
        module_name = input("Enter Module Name: ")
        course_code = input("Enter Course Code: ")
        department = input("Enter Department: ")
        lecturer_email = input("Enter Lecturer Email: ")
        lecturer_name = input("Enter Lecturer Name: ")
        lecturer_department = input("Enter Lecturer Department: ")
        lecturer_staff_id = input("Enter Lecturer Staff ID: ")
        lecturer_speciality = input("Enter Lecturer Speciality: ")
        lecturer_qualification = input("Enter Lecturer Qualification: ")
        print()

        try:
            # Create a new Lecturer object
            lecturer = Lecturer(lecturer_email, lecturer_name, lecturer_department,
                                lecturer_staff_id, lecturer_speciality, lecturer_qualification)

            # Create a new Module object and add it to the list
            module = Module(module_id, lecturer, module_name,
                            course_code, department)

            module_list.append(module)

            print("\nModule added successfully\n")

        except ValueError as e:
            print(e)

    # fucntion to add students to  the module
    def add_students_to_module(modules_list):
        module_id = input("Enter the Module Id to add the student(s) to: ")

        add_method = input(
            "Enter 'file' to automatically add students from a file, or 'input' to manually add students from user input: ")
        while add_method != "file" and add_method != "input":
            add_method = input("Invalid input. Enter 'file' or 'input': ")

        if add_method == "file":
            file_name = input(
                "Enter the file name to read the students from: ")
            for module in modules_list:
                if module.get_module_id() == module_id:
                    department = module.get_department()
            class_list = Student.auto_add_classlist(file_name, department)
        else:
            class_list = []
            while True:
                email_address = input("Enter student's email address: ")
                name = input("Enter student's name: ")
                department = input("Enter student's department: ")
                student_number = int(
                    input("Enter student's number (MUST BE 9 Digits in Length): "))
                programme_code = input("Enter student's programme code: ")
                programme_year = int(input("Enter student's programme year: "))
                student_type = input("Enter student's student type: ")

                grades_input = input(
                    "Do you want to enter grades for this student? (y/n)")
                if grades_input.lower() == 'y':
                    list_of_grades = input(
                        "Enter student's list of grades (comma-separated): ")
                    grades = list_of_grades.split(",")
                else:
                    grades = "None"

                student = Student(email_address, name, department, student_number,
                                  programme_code, programme_year, student_type, grades)
                class_list = Student.append_to_class_list(class_list, student)

                add_another = input("Add another student? (y/n) ")
                if add_another != "y":
                    break

        # Add students to module
        found_module = False
        for module in modules_list:
            if module.get_module_id() == module_id:
                found_module = True
                for student in class_list:
                    module.add_student(student)
                print(f"\n{len(class_list)} students added to module {module_id}")
                break

        if not found_module:
            print(f"No module found with ID {module_id}")

    # fucntion to add studend's grade to module

    def add_student_grades_to_module(module_list):
        module_id = input(
            "Enter the module ID to add the student grade details to: ")
        num_grades = int(input("How many grades do you want to enter? "))

        # Loop through and prompt user to enter student grade details
        for i in range(num_grades):
            print("\nAdding grade details for Student {}".format(i+1))
            student_number = input("Enter student number: ")
            assessment_name = input("Enter assessment name: ")
            percentage_achieved = int(input("Enter percentage achieved: "))

            # Convert percentage to grade using GradeCalculator class
            grade = GradeCalculator.percentage_to_grade(
                percentage_achieved)

            # Create list with student grade details
            student_grade = [student_number,
                             assessment_name, percentage_achieved, grade]

            # Append to assessment list in the Module class
            for module in module_list:
                if module.get_module_id() == module_id:
                    module.append_to_assessment_list(student_grade)
                    break
        print("\nGrades added successfully!")

    # function to display modules details
    def display_modules(modules_list):
        print("\n*----------------------------------------------------------------*")
        for module in modules_list:
            print(
                f"ModuleID: {module.get_module_id()}\nModule Course Code: {module.get_course_code()}\nModule Name: {module.get_module_name()}\nMdoule Department: {module.get_department()}\n\n")

        total_modules = len(modules_list)
        total_students = sum(len(module.get_class_list())
                             for module in modules_list)
        modules_by_department = {}
        for module in modules_list:
            if module.get_department() in modules_by_department:
                modules_by_department[module.get_department()] += 1
            else:
                modules_by_department[module.get_department()] = 1

        print(f"\nTotal number of modules in the system: {total_modules}")
        print(f"Total number of students in the system: {total_students}")
        print("Total number of modules in the system, by department:")
        for department, count in modules_by_department.items():
            print(f"{department}: {count}")

        print("\n*----------------------------------------------------------------*")

    # fuction to display list of stduden according to given module ID

    def display_list_of_students(module_list):
        module_id = input("Enter the module ID: ")
        found_module = False
        for module in module_list:
            if module.get_module_id() == module_id:
                found_module = True
                print(
                    "\n*----------------------------------------------------------------*")
                print(
                    f"\nModule: {module.get_module_name()}\nDepartment: {module.get_department()}\nLecturer: {module.get_lecturer().get_name()}\n")
                class_list = module.get_class_list()
                if len(class_list) == 0:
                    print("No students enrolled in this module.")
                else:
                    for student in class_list:
                        print(student)
                        print()
                    print(
                        f"\nTotal number of students in this module: {len(class_list)}")
                    print(
                        "\n*----------------------------------------------------------------*")

                break
        if not found_module:
            print("Module not found.")

    # function to display list of students grades
    def display_list_of_students_grades(module_list):
        module_id = input("Enter the Module Id: ")
        module_found = False
        for module in module_list:
            if module.get_module_id() == module_id:
                module_found = True
                assessment_list = module.get_assessment_list()
                if assessment_list:
                    total_students = sum(len(module.get_class_list())
                                         for module in module_list)
                    print("Student number\t\tAssessment\tGrade Percentage\tGrade")
                    total = 0
                    highest = 0
                    lowest = 100
                    num_a = 0
                    num_b_plus = 0
                    num_b = 0
                    num_b_minus = 0
                    num_c_plus = 0
                    num_c = 0
                    num_d = 0
                    num_f = 0
                    count = 0
                    for i in range(0, len(assessment_list), 4):
                        student_num = assessment_list[i]
                        assessment_name = assessment_list[i+1]
                        grade_percentage = int(assessment_list[i+2])
                        grade = assessment_list[i+3]
                        total += grade_percentage
                        count += 1
                        if grade_percentage > highest:
                            highest = grade_percentage
                        if grade_percentage < lowest:
                            lowest = grade_percentage
                        if grade == "A":
                            num_a += 1
                        elif grade == "B+":
                            num_b_plus += 1
                        elif grade == "B":
                            num_b += 1
                        elif grade == "B-":
                            num_b_minus += 1
                        elif grade == "C+":
                            num_c_plus += 1
                        elif grade == "C":
                            num_c += 1
                        elif grade == "D":
                            num_d += 1
                        elif grade == "F":
                            num_f += 1
                        print(
                            f"{student_num}\t\t{assessment_name}\t\t{grade_percentage}\t\t\t{grade}")
                    average = total / count
                    print("\nSummary Statistics:")
                    print(f"Total:\t\t\t{total_students}")
                    print(f"Highest:\t\t{highest}")
                    print(f"Lowest:\t\t\t{lowest}")
                    print(f"Average:\t\t{average:.1f}")
                    print(f"A:\t\t\t{num_a}")
                    print(f"B+:\t\t\t{num_b_plus}")
                    print(f"B:\t\t\t{num_b}")
                    print(f"B-:\t\t\t{num_b_minus}")
                    print(f"C+:\t\t\t{num_c_plus}")
                    print(f"C:\t\t\t{num_c}")
                    print(f"D:\t\t\t{num_d}")
                    print(f"F:\t\t\t{num_f}")
                    break
                else:
                    print("\nNo Assessment List found for students in this Module")

        if not module_found:
            print("\nModule not found.")

    def on_exit(modules_list):
        with open('updated_modules.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ModuleId', 'ModuleName', 'CourseCode', 'Department',
                             'Lecturer_Email', 'Lecturer_Name', 'Lecturer_StaffId',
                             'Lecturer_Speciality', 'Lecturer_Qualification'])
            for module in modules_list:
                writer.writerow([module.get_module_id(), module.get_module_name(), module.get_course_code(),
                                 module.get_department(), module.get_lecturer().get_email_address(),
                                module.get_lecturer().get_lecturer_name(), module.get_lecturer().get_staff_id(),
                                module.get_lecturer().get_speciality(), module.get_lecturer().get_qualification()])

    # function to display basic information of system

    def display_baic_info(modules_list):

        total_modules = len(modules_list)
        total_students = sum(len(module.get_class_list())
                             for module in modules_list)
        modules_by_department = {}
        for module in modules_list:
            if module.get_department() in modules_by_department:
                modules_by_department[module.get_department()] += 1
            else:
                modules_by_department[module.get_department()] = 1

        print("\n*----------------------------------------------------------------*")
        print(f"\nTotal number of modules in the system: {total_modules}")
        print(f"Total number of students in the system: {total_students}")
        print("Total number of modules in the system, by department:")
        for department, count in modules_by_department.items():
            print(f"{department}: {count}")
        print("\n*----------------------------------------------------------------*")

    # calling display_modules to give us information about added modules in the system

    print("\nCurrently Added Modules & their Details: ")
    display_modules(module_list)
    # Display the menu
    while True:

        print("\nWhat Would You Like to do:\n"
              "1. Add Module\n"
              "2. Add students to Module\n"
              "3. Add student grades to Module\n"
              "4. Display list of all Modules \n"
              "5. Display List of Students\n"
              "6. Display List of Students Grades\n"
              "7. Exit")

        choice = input("\nEnter your choice (1-7): ")
        print()

        if choice == "1":
            add_module()
            display_modules(module_list)
        elif choice == "2":
            add_students_to_module(module_list)
            display_baic_info(module_list)
        elif choice == "3":
            add_student_grades_to_module(module_list)
            display_baic_info(module_list)
        elif choice == "4":
            display_modules(module_list)
        elif choice == "5":
            display_list_of_students(module_list)
        elif choice == "6":
            display_list_of_students_grades(module_list)
        elif choice == "7":
            on_exit(module_list)
            print("Updated modules.csv File Created, Now Exiting........")
            print("Thank You for Using Our E-Learning Portal !")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
