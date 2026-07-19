students = []
id = 100

def add_student():
    global id
    while True:
        student_name = input("Enter Student Name: ")
        if student_name == "":
            print("Name can't be empty , please enter student name: ")
        else:
            break
    while True:
        try:
            student_age = int(input("Enter Student Age: "))
            if student_age <= 3:
                print("Minimum age requirment is 3, try again! ")
            else:
                break
        except:
            print("Enter Age in number! ")
    while True:
        try:
            student_class = int(input("Enter Student Class: "))

            if student_class < 1:
                print("Minimum class requirment is 1 , try again! ")
            else:
                break

        except:
            print("Type class in numbers only! ")

    id += 1
    student_id = id

    new_student = Student(student_name, student_age, student_class, student_id)

    students.append(new_student)

    print("Student Added! ")
    input("Enter to continue! ")

def remove_student(students):
    if students:
        all_students(students)
        print("HERE ARE ALL THE STUDENTS LIST, CHOOSE THE STUDENT NUMBER TO REMOVE STUDENT! ")

        while True:
            try:
                profile = int(input("Enter the Student Number you wanna remove: "))
                students.pop(profile - 1)
                print(f"Student {profile} has removed!")
                input("Enter to continue! ")
                break
            except:
                print("Enter valid Student Number to procced! ")

    else:
        print("No Student found! ")
        input("Enter to continue! ")

def all_students(students):
    for i in range(len(students)):
        print(f"Student {i+1}")
        students[i].show_students()
        print("---------------------------------")


def menu():
    print("---------------------------------")
    print("1. Add Students")
    print("2. Show Students")
    print("3. Change Student Name")
    print("4. Change Student Age")
    print("5. Change Student Class")
    print("6. Remove Student")
    print("---------------------------------")
    print("7. Exit")

def operation(choice, students):
    if choice == 1:
        add_student()
    
    elif choice == 2:
        if students:
            all_students(students)
            input("Enter to continue! ")
        else:
            print("No Students found! ")
            input("Enter to continue! ")
        
    elif choice == 3:
        if students:
            all_students(students)
            print("HERE ARE ALL THE STUDENTS LISTS , CHOOSE THE STUDENT NUMBER TO UPDATE NAME! ")

            while True:
                try:
                    student = int(input("Enter the Student Number to update Name: "))
                    while True:
                        new_name = input("Enter the name you wanna update: ")
                        if new_name == "":
                            print("Name can't be empty, please type student name! ")
                        else:
                            break

                    students[student - 1].change_name(new_name)
                    print("Student name has updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only Student Number, Try again! ")

        else:
            print("No student found! ")
            input("Enter to continue! ")

    elif choice == 4:
        if students:
            all_students(students)
            print("HERE ARE ALL THE STUDENTS LISTS , CHOOSE THE STUDENT NUMBER TO UPDATE AGE! ")

            while True:
                try:
                    student = int(input("Enter the Student Number to update Age: "))
                    while True:
                        try:
                            new_age = int(input("Enter the Age you wanna update: "))

                            if new_age <= 3:
                                print("Minimum Age requirment is 3, try again! ")
                            else:
                                break
                        except:
                            print("Type age in numbers! ")

                    students[student - 1].change_age(new_age)
                    print("Student Age has updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only Student Number, Try again! ")

        else:
            print("No student found! ")
            input("Enter to continue! ")

    elif choice == 5:
        if students:
            all_students(students)
            print("HERE ARE ALL THE STUDENTS LISTS , CHOOSE THE STUDENT NUMBER TO UPDATE CLASS! ")

            while True:
                try:
                    student = int(input("Enter the Student Number to update Class: "))
                    while True:
                        try:
                            new_class = int(input("Enter the Class you wanna update: "))
                            if new_class < 1:
                                print("Minimum class requirment is 1, try again! ")
                            else:
                                break

                        except:
                            print("Enter class in numbers only")

                    students[student - 1].change_class(new_class)
                    print("Student Class has updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only Student Number, Try again! ")

        else:
            print("No student found! ")
            input("Enter to continue! ")

    elif choice == 6:
        remove_student(students)

            
    elif choice == 7:
        return True

class Student:
    def __init__(self, name, age, classs, student_id):
        self.name = name
        self.age = age
        self.classs = classs
        self.student_id = student_id

    def show_students(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Class : {self.classs}")
        print(f"Student ID : {self.student_id}")

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age


    def change_class(self, new_class):
        self.classs = new_class

while True:
    while True:
        try:
            menu()
            exit = False
            choice = int(input("\nWhat operation you wanna do: "))
            exit = operation(choice, students)

            if exit:
                break
            else:
                continue
        except:
            print("Only type operation number to continue! ")

    break



