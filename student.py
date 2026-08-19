from file_handling import load_data, save_data

class Student:
    def __init__(self, name= "", roll_no= "", branch = "", marks = 0):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def input_stu (self, students):
        while True:
            name = input("Enter your name:")
            found = False
            try:
                roll_no = int(input("Enter your roll number:")) 
                found = False
                for student in students:
                    if student["roll_no"] == roll_no:
                        print("Roll number already exists")
                        found = True
                        break
                if found == True:
                    continue
            except ValueError:
                print("Invalid Input")
                print("-" * 20)
                continue
            branch = input("Enter your Branch:")
            try:
                marks = int(input("Enter your marks:"))
            except ValueError:
                print("Invalid Input")
                print("-" * 20)
                continue
            print("-" * 20)
            stu = {
                "name": name,
                "roll_no": roll_no,
                "branch": branch,
                "marks": marks
            }
            students.append(stu)
            print("Student added successfully!")
            print("-" * 20)
            break
        save_data(students)

    def view_stu(self, students):
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("-" * 20)
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Branch:", student["branch"])
                print("Marks:", student["marks"])
                print("-" * 20)
            print("Total students:", len(students))

    def search_stu (self, students):
        while True:
            try:
                roll = int(input("Enter roll number of student to search: "))    
            except ValueError:
                print("Invalid Input")
                print("-" * 20)
                continue
            found = False
            for student in students:
                if(student["roll_no"] == roll):
                    print("Name:", student["name"])
                    print("Roll No:", student["roll_no"])
                    print("Branch:", student["branch"])
                    print("Marks:", student["marks"])
                    print("-" * 20)
                    found = True
                    break
            if found == False:
                print("Student not found")
            break

    def del_stu(self, students):
        while True:
            try:
                roll = int(input("Enter roll number of student to delete: "))
            except ValueError:
                print("Invalid Input")
                print("-" * 20)
                continue
            found = False
            for student in students:
                if(student["roll_no"] == roll):
                    students.remove(student)
                    save_data(students)
                    print("Student deleted successfully!")
                    print("-" * 20)
                    found = True
                    break    
            if found == False:
                print("Not a valid roll number for any student")
            break

    def update_stu(self, students):
        while True:
            try:
                roll = int(input("Enter roll number of student to Update: "))    
            except ValueError:
                print("Invalid Input")
                print("-" * 20)
                continue
            found = False
            for student in students:
                if (student["roll_no"] == roll):
                    name = input("Enter your name:")
                    try:
                        roll_no = int(input("Enter your roll number:"))    
                    except ValueError:
                        print("Invalid Input")
                        print("-" * 20)
                        continue
                    branch = input("Enter your Branch:")
                    try:
                        marks = int(input("Enter your marks:"))
                    except ValueError:
                        print("Invalid Input")
                        print("-" * 20)
                        continue
                    print("-" * 20)
                    student["name"] = name
                    student["roll_no"] = roll_no
                    student["branch"] = branch
                    student["marks"] = marks
                    print("Student Updated successfully!")
                    print("-" * 20)
                    save_data(students)
                    found = True
                    break
            if found == False:
                print("Student not exist")
            break