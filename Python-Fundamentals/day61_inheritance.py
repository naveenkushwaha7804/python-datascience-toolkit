# ============================================================
# INHERITANCE
# ============================================================

# ============================================================
# 1. SINGLE LEVEL INHERITANCE
# ============================================================

class Parent:
    x = 10

    def home(self):
        print("This is the parent home")


class Child(Parent):
    def home(self):
        print("This is the child home")
        super().home()  # Calls parent class method


obj = Child()

print(obj.x)
obj.home()


# ============================================================
# 2. MULTI-LEVEL INHERITANCE
# ============================================================

class GrandParent:
    x = 10

    def home(self):
        print("This is the grandparent home")


class Parent(GrandParent):
    def home(self):
        print("This is the parent home")
        super().home()


class Child(Parent):
    def home(self):
        print("This is the child home")
        super().home()


obj = Child()

print(obj.x)
obj.home()


# ============================================================
# 3. MULTIPLE INHERITANCE
# ============================================================

class Father:
    def home(self):
        print("Father's home")


class Mother:
    def home(self):
        print("Mother's home")


class Child(Father, Mother):
    def home(self):
        print("Child's home")
        super().home()


obj = Child()
obj.home()

# MRO (Method Resolution Order)
print(Child.mro())


# ============================================================
# 4. HIERARCHICAL INHERITANCE
# ============================================================

class A:
    def home(self):
        print("From class A")


class B(A):
    def home(self):
        print("From class B")
        super().home()


class C(A):
    def home(self):
        print("From class C")
        super().home()


obj1 = B()
obj2 = C()

obj1.home()
obj2.home()


# ============================================================
# 5. HYBRID INHERITANCE
# ============================================================

class A:
    def show(self):
        print("From class A")


class B(A):
    def show(self):
        print("From class B")
        super().show()


class C(A):
    def show(self):
        print("From class C")
        super().show()


class D(B, C):
    def show(self):
        print("From class D")
        super().show()


obj = D()
obj.show()

# Method Resolution Order
print(D.mro())