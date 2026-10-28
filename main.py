students= []
Courses= set()
while True:
    print("STUDENT REGISTRATION SYSTEM")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. View Available Courses")
    print("7. Exit")
    choice = input("Select an option: ")
    if choice=="1":
        reg_number = input("Enter registration number: ")
        duplicate_found = False
        for s in students:
            if s["reg-number"] == reg_number:
                duplicate_found = True
                break

        if duplicate_found:
            print("Error: Registration Number already exists")
        else:
            name = input("Enter name: ")

            age_input= input("Enter age: ")
            if age_input.isdigit():
                age = int(age_input)
            else:
                age = 0

            course = input("Enter course: ")

            student = { "name": name, "age": age, "reg-number": reg_number, "course": course}

            students.append(student)
            Courses.add(course)
            print("Student registered successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No students registered yet.")
        else:
            print("REGISTERED STUDENTS")
            for s in students:
                print(f"name, {s['name']}")
                # print(f"Name: {s['name']} | Age: {s['age']} | Reg Number: {s['reg_number']} | Course: {s['course']}")
            print(f"Total registered students: {len(students)}")

    elif choice == "3":
        search_reg = input("Search Student's registration number: ")
        found_student = None

        for s in students:
            if s["reg-number"] == search_reg:
                found_student = s
                break

        if found_student is not None:
            print("Student Found: ")
            print(f"Name: {found_student['name']}")
            print(f"Age: {found_student['age']}")
            print(f"Registration Number: {found_student['reg-number']}")
            print(f"Course: {found_student['course']}")
        else:
            print("Student not found")

    elif choice == "4":
        update_reg = input("Update Student's registration number: ")
        found_student = None


        for s in students:
            if s["reg-number"] == update_reg:
                found_student = s
                break

        if found_student is not None:
            new_course = input("Enter new course: ")
            found_student["course"] = new_course

            Courses.clear()
            for s in students:
                Courses.add(s["course"])

            print("Student course updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        remove_reg = input("Student's Registration Number to remove: ")
        student_to_remove = None

        for s in students:
            if s["reg-number"] == remove_reg:
                student_to_remove = s
                break

        if student_to_remove is not None:
            students.remove(student_to_remove)

            Courses.clear()
            for s in students:
                Courses.add(s["course"])

            print(f"Student removed successfully! Updated total students: {len(students)}")
        else:
            print("Student not found.")

    elif choice == "6":
        if len(Courses) == 0:
            print("No courses available.")
        else:
            print("AVAILABLE COURSES")
            for c in Courses:
                print(c)
            print(f"Total Unique Courses: {len(Courses)}")

    elif choice == "7":
        print("Exiting Student Registration System. Goodbye!")
        running = False

    else:
        print("Invalid option. Please pick a number from 1 to 7.")


