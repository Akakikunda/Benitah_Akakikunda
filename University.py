import random

# ---------- Course Class ----------
class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

# ---------- Student Class ----------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.registered = False
        self.registration_number = None
        self.courses = []
        self.marks = {}

    def register(self):
        if not self.registered:
            self.registration_number = "REG" + str(random.randint(1000, 9999))
            self.registered = True
            print(f"\n{self.name} registered successfully! Registration Number: {self.registration_number}\n")
        else:
            print("Already registered.")

    def choose_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.name}' added successfully.")

    def add_mark(self, course_code, mark):
        self.marks[course_code] = mark

    def view_marks(self):
        if not self.marks:
            print("No marks entered yet.")
        else:
            print("\n--- Marks ---")
            for code, mark in self.marks.items():
                print(f"{code}: {mark}")

    def print_report(self):
        print("\n--- Student Report ---")
        print(f"Name: {self.name}")
        print(f"Registration Number: {self.registration_number}")
        print("Courses and Marks:")
        for course in self.courses:
            mark = self.marks.get(course.code, "Not marked yet")
            print(f" * {course.name} ({course.code}): {mark}")
        print("------------------------\n")

# ---------- University Class ----------
class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.available_courses = [
            Course("CSE101", "Computer Science"),
            Course("MAT101", "Mathematics"),
            Course("PHY101", "Physics"),
        ]

    def apply(self, name, age):
        student = Student(name, age)
        self.students.append(student)
        print(f"\nApplication successful for {name}!\n")
        return student

# ---------- Main Menu ----------
def main():
    uni = University("Benitah University")
    current_student = None

    while True:
        print("====== University System Menu ======")
        print("1. Apply to the University")
        print("2. Register")
        print("3. Choose Courses")
        print("4. Add/View Marks")
        print("5. Print Report")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            current_student = uni.apply(name, age)

        elif choice == "2":
            if current_student:
                current_student.register()
            else:
                print("You need to apply first.")

        elif choice == "3":
            if current_student and current_student.registered:
                print("\nAvailable Courses:")
                for i, course in enumerate(uni.available_courses):
                    print(f"{i+1}. {course.name} ({course.code})")
                course_choice = int(input("Choose course number to add: "))
                if 1 <= course_choice <= len(uni.available_courses):
                    current_student.choose_course(uni.available_courses[course_choice - 1])
                else:
                    print("Invalid course selection.")
            else:
                print("Please register first.")

        elif choice == "4":
            if current_student and current_student.registered:
                print("\n1. Add Marks")
                print("2. View Marks")
                sub_choice = input("Choose an option: ")
                if sub_choice == "1":
                    for course in current_student.courses:
                        try:
                            mark = int(input(f"Enter mark for {course.name} ({course.code}): "))
                            current_student.add_mark(course.code, mark)
                        except ValueError:
                            print("Invalid input. Enter a number.")
                elif sub_choice == "2":
                    current_student.view_marks()
                else:
                    print("Invalid option.")
            else:
                print("Please register and choose courses first.")

        elif choice == "5":
            if current_student and current_student.registered:
                current_student.print_report()
            else:
                print("Please register first.")

        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# ---------- Run Program ----------
if __name__ == "__main__":
    main()
