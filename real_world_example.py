#real world example using method overriding, method overloading, and MRO
class Teacher:
    def teach(self):
        print("Teaching in classroom...")

class OnlineTeacher(Teacher):
    def teach(self):  # Overriding
        print("Teaching on Zoom...")

    def greet(self, name=None):  # Simulating overloading
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello, students!")

t = OnlineTeacher()
t.teach()         # Teaching on Zoom... (Overriding)
t.greet()         # Hello, students!
t.greet("Ben")    # Hello, Ben!
