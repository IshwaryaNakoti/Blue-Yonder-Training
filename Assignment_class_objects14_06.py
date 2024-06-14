#1
class Students:
    def __init__(self, name, age, grade) -> None:
        self.name = name 
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"Student details: \n1.Name = {self.name}\n2.Age = {self.age}\n3.Grade = {self.grade}")
#2
class StudentsCheckValidity:
    pass

#3
class Staff:
    def __init__(self, role, dept, salary) -> None:
        self.role = role
        self.dept = dept 
        self.salary = salary
    
    def display(self):
        print(f"Staff details:\n1. Role = {self.role}\n2. Department = {self.dept}\n3. Salary = {self.salary}")
class Teacher(Staff):
    def __init__(self, role, dept, salary, name, age) -> None:
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRole: {self.role}\nDepartment: {self.dept}")

#4
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def vehicleFair(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
    
    def busfair(self):
        return (self.capacity * 100) + (self.capacity * 10)
 #5-a   
class Jets:

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class F14(Jets):
    def __init__(self, name = 'F14', country = 'USA'):
        super().__init__(name, country)

#5-b
class F16(Jets):
    def __init__(self, name = 'F16', country = 'USA'):
        super().__init__(name, country)
        self.engine = 2
        self.seat = 2
        self.tail = 2
          
def one():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age : "))
        grade = eval(input("Enter your CGPA (/10) : "))
        s = Students(name, age, grade)
        s.display()
    except Exception as e:
        print("Error occured - ", e)

def two():
    student_instance = StudentsCheckValidity()
    print("Type : ", type(student_instance))
    print(student_instance)

def three():
    teacher = Teacher("VP", "Maths", 25000, "Ishwarya", 23)
    teacher.show_details()

def four():
    name = input("Enter vehicle name: ")
    mileage = input("Enter mileage: ")
    capacity = eval(input("Enter capacity of the vehicle: "))
    b = Bus(name, mileage, capacity)
    print(f"Total bus fare is : {b.busfair()}")

#5-a
def five():
    a = F14()
    print("Origin = ",a.origin)
    print("Name = ",a.name)

#5-b
def six():
    a = F16()
    print("Origin = ",a.origin)
    print("Name = ",a.name)
    print("Engine = ", a.engine)

if __name__ == '__main__':
    print("14-06-2024 - Python Training - Blue Yonder Assignment 4:")
    print("Assignments On Classes and objects")
    print("\n1. Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object")
    print("\n2. Write a Program to create a valid empty class with the name Students, with no properties.")
    print("\n3. Fetch Parent class details in child class using an instance method")
    print("\n4. Method Overriding - single inheritance ")
    print("\n5. Default values in a constructor")
    print("\n6. Default params in child class")
    print("\n7. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 7:
        if n == 1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : five()
        elif n==6 : six()
        n = int(input("\n  Enter a choice: "))