from student import Student
from file_handling import load_data, save_data

stu = Student()
students = load_data()
while True:
    try:
        menu = int(input(
        "1. Add Student\n"
        "2. View Student\n"
        "3. Search Student\n"
        "4. Delete Student\n"
        "5. Update Student\n"
        "6. Exit\n"
        "Enter your choice: "
        ))
    except ValueError:
        print("Invalid Input")
        print("-" * 20)
        continue
    if menu == 1:
        stu.input_stu(students)
    elif menu == 2:
        stu.view_stu(students)

    elif menu == 3:
        stu.search_stu(students)
    elif menu == 4:
        stu.del_stu(students)
    elif menu == 5:
          stu.update_stu(students)
    elif menu == 6:
        print("Thankyou")
        break
    else:
        print("Invalid choice")