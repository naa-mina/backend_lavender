#Dictionary that contains students information
student_system = {}
print("Welcome to Students Management System")

#Prompt the user about options avaiable
#print("Choose an option: \n 1.Add a Student, collect (name, age, grade and a list of courses) \n 2.Remove a Student \n 3.View one student \n 4.View all students \n 5.Exit")
print()

  
while True:
        print("Choose an option: \n 1.Add a Student, collect (name, age, grade and a list of courses) \n 2.Remove a Student \n 3.View one student \n 4.View all students \n 5.Exit")

        user_input = input("Please enter your choice: ")
        print()
        
        #add student information
        if user_input == "1":
            student_name = input("Enter student name: ").strip().title()
            student_age = input("Enter student age: ")
            student_grade = input("Enter student grade: ").strip().title()
            student_course = input("Enter student course: ").strip().title()
            print(f"{student_name} has been added to the system")
            #store student details in nested dictionary
            student_system[student_name] = {"name": student_name , "age": student_age , "grade": student_grade , "course": student_course }
            print()

        #remove students in the system
        elif user_input == "2":
            remove_student = input("Enter student name to remove: ").strip().title()
            if remove_student in student_system:
                del student_system[remove_student]
                print(f"{remove_student} has been removed from the system")
                print()
            else:
                print(f"{remove_student} not in system")
                print()
        #view one student
        elif user_input == "3":
            view_student = input("Enter name of student to view: ").strip().title()
            if view_student in student_system:
                student_details = student_system[view_student]
                print(f'- {student_name}, Age: {student_details["age"]}, Grade: {student_details["grade"]}, Course: {student_details["course"]}')
            else:
                print(f"{view_student} not in system")
        # view all students in system
        elif user_input == "4":
            print("Students in the system: ")
            # using a for loop to iterate through the dictonary, remember it's key,value
            for student_name,value in student_system.items():
                print(f'- {student_name}, Age: {value["age"]}, Grade: {value["grade"]}, Course: {value["course"]}')
            print()
        # Exit program
        elif user_input == "5":
            print("Goodbye !")
            #Adding break to end program
            break
        else:
            print("You entered an invalid choice")

