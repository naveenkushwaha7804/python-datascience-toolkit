# OOP - Object Oriented Programming

# ============================================================
# 1. CLASS AND OBJECT
# ============================================================

class Student:
    def __init__(self):
        print("Constructor called")
        print(id(self))


obj = Student()
print(id(obj))


# ============================================================
# 2. CLASS VARIABLES AND METHODS
# ============================================================

class Student:
    school = "GBHSC"
    school_city = "Dobhi"

    def detail(self):
        print("Student belongs to the school")


obj = Student()

print(obj.school)
print(Student.school)
print(obj.school_city)

obj.detail()


# ============================================================
# 3. CONSTRUCTOR AND INSTANCE VARIABLES
# ============================================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(self.name, self.age, self.grade)


obj = Student("Naveen", 21, "B.Tech")
obj.display()


# ============================================================
# 4. INSTANCE VARIABLES
# ============================================================

class Student:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def add_new(self, roll_no):
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.contact, self.roll_no, self.email)


obj = Student("Naveen", 7804059040)

obj.add_new(101)
obj.email = "naveenkushwaha@gmail.com"

obj.display()

obj1 = Student("Rahul", 9302123123)

print(obj.name)
print(obj1.name)


# ============================================================
# 5. CLASS VARIABLES
# ============================================================

class Student:
    school_name = "SPHSS"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

        Student.school_city = "Bhopal"

        print(
            Student.school_name,
            Student.school_city,
            self.name,
            self.roll_no
        )

    def add_new(self):
        Student.school_code = 101
        print(Student.school_code)


Student.contact = 347837478

obj = Student("Naveen", 1023)
obj.add_new()

print(obj.name)


# ============================================================
# 6. LOCAL VARIABLES
# ============================================================

class Student:
    def __init__(self):
        x = 10
        print(x)

    def new(self):
        y = 20
        z = y + 10
        print(z)


obj = Student()
obj.new()


# ============================================================
# 7. CLASS METHOD
# ============================================================

class Student:
    grade = "10th"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def update_grade(cls, new_grade):
        cls.grade = new_grade

    @classmethod
    def add_code(cls, code):
        cls.code = code


obj = Student("Naveen", "0127CD231323")

print(Student.grade)

obj.update_grade("12th")
print(Student.grade)

obj.add_code("1232234")
print(Student.code)

print(obj.name)


# ============================================================
# 8. STATIC METHOD
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def greet(name):
        print(f"Welcome {name} to my web page")


obj = Student("Naveen")
obj.greet(obj.name)


# ============================================================
# OOP CONCEPTS
# ============================================================

"""
1. Abstraction
   - Abstract Class
   - Abstract Method
   - Concrete Method

2. Encapsulation
   - Public Variable/Method
   - Protected Variable/Method
   - Private Variable/Method

3. Inheritance
   - Code Reusability
   - Types of Inheritance
   - Method Overriding
   - MRO (Method Resolution Order)
   - super()

4. Polymorphism
   - Compile-Time Polymorphism
   - Runtime Polymorphism
   - Method Overloading
   - Method Overriding
"""