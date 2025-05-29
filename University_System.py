class Person:
    """Parent class representing a person in the university system"""
    
    def __init__(self, name, age, id_number, email):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
    
    def display_info(self):
        """Display basic person information"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID Number: {self.id_number}")
        print(f"Email: {self.email}")
    
    def __str__(self):
        return f"Person: {self.name} (ID: {self.id_number})"


class Student(Person):
    """Student subclass inheriting from Person"""
    
    def __init__(self, name, age, id_number, email, student_id, major, year, gpa=0.0):
        super().__init__(name, age, id_number, email)
        self.student_id = student_id
        self.major = major
        self.year = year
        self.gpa = gpa
        self.courses = []
    
    def add_course(self, course):
        """Add a course to the student's course list"""
        self.courses.append(course)
    
    def display_info(self):
        """Display student information"""
        print("=" * 40)
        print("STUDENT INFORMATION")
        print("=" * 40)
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Year: {self.year}")
        print(f"GPA: {self.gpa:.2f}")
        if self.courses:
            print(f"Enrolled Courses: {', '.join(self.courses)}")
        else:
            print("Enrolled Courses: None")
    
    def __str__(self):
        return f"Student: {self.name} - {self.major} (Year {self.year})"


class Lecturer(Person):
    """Lecturer subclass inheriting from Person"""
    
    def __init__(self, name, age, id_number, email, employee_id, department, specialization, salary):
        super().__init__(name, age, id_number, email)
        self.employee_id = employee_id
        self.department = department
        self.specialization = specialization
        self.salary = salary
        self.courses_taught = []
    
    def add_course(self, course):
        """Add a course to the lecturer's teaching list"""
        self.courses_taught.append(course)
    
    def display_info(self):
        """Display lecturer information"""
        print("=" * 40)
        print("LECTURER INFORMATION")
        print("=" * 40)
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Specialization: {self.specialization}")
        print(f"Salary: ${self.salary:,.2f}")
        if self.courses_taught:
            print(f"Courses Teaching: {', '.join(self.courses_taught)}")
        else:
            print("Courses Teaching: None")
    
    def __str__(self):
        return f"Lecturer: {self.name} - {self.department} Department"


class Staff(Person):
    """Staff subclass inheriting from Person"""
    
    def __init__(self, name, age, id_number, email, employee_id, position, department, salary):
        super().__init__(name, age, id_number, email)
        self.employee_id = employee_id
        self.position = position
        self.department = department
        self.salary = salary
        self.responsibilities = []
    
    def add_responsibility(self, responsibility):
        """Add a responsibility to the staff member"""
        self.responsibilities.append(responsibility)
    
    def display_info(self):
        """Display staff information"""
        print("=" * 40)
        print("STAFF INFORMATION")
        print("=" * 40)
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        if self.responsibilities:
            print(f"Responsibilities: {', '.join(self.responsibilities)}")
        else:
            print("Responsibilities: None assigned")
    
    def __str__(self):
        return f"Staff: {self.name} - {self.position}"


class UniversitySystem:
    """Main class to manage the university system"""
    
    def __init__(self):
        self.people = []
    
    def get_basic_info(self):
        """Get basic person information from user"""
        print("\nEnter basic information:")
        name = input("Name: ").strip()
        while True:
            try:
                age = int(input("Age: "))
                if age < 0:
                    print("Age cannot be negative. Please enter a valid age.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for age.")
        
        id_number = input("ID Number: ").strip()
        email = input("Email: ").strip()
        
        return name, age, id_number, email
    
    def create_student(self):
        """Create a new student with user input"""
        print("\n=== Creating New Student ===")
        name, age, id_number, email = self.get_basic_info()
        
        student_id = input("Student ID: ").strip()
        major = input("Major: ").strip()
        
        while True:
            try:
                year = int(input("Year (1-4): "))
                if year < 1 or year > 4:
                    print("Year must be between 1 and 4.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for year.")
        
        while True:
            try:
                gpa = float(input("GPA (0.0-4.0): "))
                if gpa < 0.0 or gpa > 4.0:
                    print("GPA must be between 0.0 and 4.0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for GPA.")
        
        student = Student(name, age, id_number, email, student_id, major, year, gpa)
        
        # Add courses
        courses_input = input("Enter courses (separate multiple courses with commas): ").strip()
        if courses_input:
            # Split by comma and clean up each course name
            courses = [course.strip() for course in courses_input.split(',') if course.strip()]
            for course in courses:
                student.add_course(course)
        
        self.people.append(student)
        print(f"\nStudent {name} created successfully!")
    
    def create_lecturer(self):
        """Create a new lecturer with user input"""
        print("\n=== Creating New Lecturer ===")
        name, age, id_number, email = self.get_basic_info()
        
        employee_id = input("Employee ID: ").strip()
        department = input("Department: ").strip()
        specialization = input("Specialization: ").strip()
        
        while True:
            try:
                salary = float(input("Salary: $"))
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for salary.")
        
        lecturer = Lecturer(name, age, id_number, email, employee_id, department, specialization, salary)
        
        # Add courses
        courses_input = input("Enter courses teaching (separate multiple courses with commas): ").strip()
        if courses_input:
            # Split by comma and clean up each course name
            courses = [course.strip() for course in courses_input.split(',') if course.strip()]
            for course in courses:
                lecturer.add_course(course)
        
        self.people.append(lecturer)
        print(f"\nLecturer {name} created successfully!")
    
    def create_staff(self):
        """Create a new staff member with user input"""
        print("\n=== Creating New Staff Member ===")
        name, age, id_number, email = self.get_basic_info()
        
        employee_id = input("Employee ID: ").strip()
        position = input("Position: ").strip()
        department = input("Department: ").strip()
        
        while True:
            try:
                salary = float(input("Salary: $"))
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for salary.")
        
        staff = Staff(name, age, id_number, email, employee_id, position, department, salary)
        
        # Add responsibilities
        responsibilities_input = input("Enter responsibilities (separate multiple responsibilities with commas): ").strip()
        if responsibilities_input:
            # Split by comma and clean up each responsibility
            responsibilities = [resp.strip() for resp in responsibilities_input.split(',') if resp.strip()]
            for responsibility in responsibilities:
                staff.add_responsibility(responsibility)
        
        self.people.append(staff)
        print(f"\nStaff member {name} created successfully!")
    
    def display_all_people(self):
        """Display information for all people in the system"""
        if not self.people:
            print("\nNo people in the system yet.")
            return
        
        print(f"\n=== ALL PEOPLE IN SYSTEM ({len(self.people)} total) ===")
        for i, person in enumerate(self.people, 1):
            print(f"\n--- Person {i} ---")
            person.display_info()
    
    def search_person(self):
        """Search for a person by name or ID"""
        if not self.people:
            print("\nNo people in the system yet.")
            return
        
        search_term = input("\nEnter name or ID to search: ").strip().lower()
        found = []
        
        for person in self.people:
            if (search_term in person.name.lower() or 
                search_term in person.id_number.lower()):
                found.append(person)
        
        if found:
            print(f"\nFound {len(found)} result(s):")
            for person in found:
                print("\n" + "-" * 40)
                person.display_info()
        else:
            print("\nNo matching records found.")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("UNIVERSITY SYSTEM MANAGEMENT")
        print("=" * 50)
        print("1. Create Student")
        print("2. Create Lecturer")
        print("3. Create Staff")
        print("4. Display All People")
        print("5. Search Person")
        print("6. Exit")
        print("-" * 50)
    
    def run(self):
        """Main program loop"""
        print("Welcome to the University System!")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.create_student()
            elif choice == '2':
                self.create_lecturer()
            elif choice == '3':
                self.create_staff()
            elif choice == '4':
                self.display_all_people()
            elif choice == '5':
                self.search_person()
            elif choice == '6':
                print("\nThank you for using the University System!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-6.")
            
            input("\nPress Enter to continue...")


def main():
    """Main function to start the university system"""
    system = UniversitySystem()
    system.run()


if __name__ == "__main__":
    main()