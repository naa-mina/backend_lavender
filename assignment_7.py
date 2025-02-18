#Dictionary that contains students information
student_system = {}
print("Welcome to Students Management System")


print()

#function to add student information
def add_student():
    student_name = input("Enter student name: ").strip().title()
    #check for duplicates
    if student_name not in student_system:
        student_age = input("Enter student age: ")
        while True:
            try:
                student_grade = float(input("Enter student grade: "))
                break #for when input is valid
            except ValueError:
                print("Enter a valid student grade, should be a number")
                

        print(f"{student_name} has been added to the system")
        #store student details in nested dictionary(ie, the value is another dictionary)
        student_system[student_name] = {"name": student_name , "age": student_age , "grade": student_grade}
        print()
    else:
        print("Student name already in system")
        print()
#function to remove student information
def remove_student():
    remove_student = input("Enter student name to remove: ").strip().title()
    if remove_student in student_system:
        del student_system[remove_student]
        print(f"{remove_student} has been removed from the system")
        print()
    else:
        print(f"{remove_student} not in system")
        print()
#function to view student
def view_student():
    view_student = input("Enter name of student to view: ").strip().title()
    if view_student in student_system:
        student_details = student_system[view_student]
        print(f'- {student_details["name"]}, Age: {student_details["age"]}, Grade: {student_details["grade"]}')
    else:
        print(f"{view_student} not in system")
#function to view all students
def view_all():
    if student_system != {}:
        print("Students in the system: ")
        # using a for loop to iterate through the dictonary, remember it's key,value that why I'm using .items()
        for student_name,value in student_system.items():
            print(f'- {student_name}, Age: {value["age"]}, Grade: {value["grade"]}')
        print()
    else:
        print("There is no student in system")
#update existing student record
def update_records():
    update_student = input("Enter name of student to update details: ").strip().title()
    if update_student in student_system:
        student_age = input("Enter student age: ")
        while True:
            try:
                student_grade = float(input("Enter student grade: "))
                break #for when input is valid
            except ValueError:
                print("Enter a valid student grade, should be a number")
            
        
        print(f"{update_student}'s details have been updated")
        student_system[update_student]["age"] = student_age
        student_system[update_student]["grade"] = student_grade
        print()
    else:
        print("Student not in system")
#calc average grade for all students
def calc_average_grades():
    if student_system == {}:
        print("No grades in system to calculate")
        return
    total_grades = sum(student["grade"] for student in student_system.values())
    average = total_grades/len(student_system)
    print(f"The average of all students is: {average:.2f}")




#function to exit program
def exit_program():
    print("Goodbye !")

while True:
    print("Choose an option: \n 1.Add a Student, collect (name, age, grade) \n 2.Update existing student records \n 3.Calculate average of students \n 4.Remove a Student \n 5.View one student \n 6.View all students  \n 7.Exit")

    user_input = input("Please enter your choice: ")
    print()
    
    
    if user_input == "1": 
        add_student()  #add student
    
    elif user_input == "2":
        update_records()  # update student record
    elif user_input == "3":
        calc_average_grades() # calc average grades of all students
    elif user_input == "4": 
        remove_student()  # remove student from record
    #view one student
    elif user_input == "5":
        view_student()

    # view all students in system
    elif user_input == "6":
        view_all()
    # Exit program
    elif user_input == "7":
        exit_program()
        break  #adding break to end program
    else:
        print("You entered an invalid choice \n")

