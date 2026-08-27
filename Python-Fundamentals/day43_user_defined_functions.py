"""
FUNCTIONS — COMPLETE NOTES + PRACTICE
======================================
def add(parameter):
    fun_body
    return value        # by default return None hota hai agar likha na jaaye
fun_name(arguments)
"""


# ---------------- BASICS: return vs print ----------------
def hello():
    print("Hello")


def add_return(x, y):
    """Return karta hai (value use kar sakte ho aage)."""
    return x + y


def add_print(x, y):
    """Sirf print karta hai, return None hota hai by default."""
    print(x + y)


# ---------------- FOR LOOP IN FUNCTION ----------------
def print_1_to_10():
    return list(range(11))


def numeric_pyramid(num):
    """1 / 12 / 123 / 1234 ... style pyramid."""
    st = ""
    for i in range(1, num + 1):
        st += str(i) + " "
        print(" " * (num - i) + st)


def fibonacci(n):
    """Fixed: original call fevibnaco() had no argument -> crash."""
    f, s = 0, 1
    result = []
    for i in range(n):
        result.append(f)
        f, s = s, f + s
    return result


# ---------------- POSITIONAL ARGUMENTS ----------------
def add3(x, y, z):
    return x + y + z
    # add3(x)        -> error: missing 2 required positional arguments
    # add3(x, y)     -> error: missing 1 required positional argument
    # add3(x, y, z, a) -> error: too many arguments


# ---------------- DEFAULT ARGUMENTS ----------------
def fun_default(x=0, y=0, z=0):
    return x + y + z
    # fun_default(12,12)    -> z defaults to 0
    # fun_default(12,12,12) -> all given
    # fun_default(2,3,4,5)  -> error: takes 0 to 3 positional arguments


# ---------------- VARIABLE-LENGTH POSITIONAL (*args) ----------------
def sum_of_lists(*args):
    """Har nested list/tuple ke andar ke numbers ka sum."""
    total = 0
    for i in args:
        for j in i:
            total += j
    return total


def show_args(*n):
    print(n)
    print(type(n))


# (*) pack data ko unpack karta hai, aur unpack data ko pack karta hai
# *  = args
# ** = kwargs


# ---------------- KEYWORD ARGUMENTS ----------------
def print_xyz(x, y, z):
    print(x)
    print(y)
    print(z)


def print_xyz_default(x=0, y=0, z=0):
    print(x)
    print(y)
    print(z)


# ---------------- VARIABLE-LENGTH KEYWORD (**kwargs) ----------------
def show_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


def explore_kwargs(**kwargs):
    for i in kwargs.keys():
        print(i)
    for i in kwargs.values():
        print(i)
    for i, j in kwargs.items():
        print("key :", i, "value", j)
    # Dictionary ke saare methods yahan apply kar sakte ho


# ---------------- COMBINED: all argument types together ----------------
def fun_combined(x, p, *z, y=0, **q):
    print("x :", x)
    print("y :", y)
    print("z :", z)
    print("p :", p)
    print("q :", q)


# ---------------- PRACTICE QUESTIONS ----------------
def natural_no(n):
    for i in range(1, n + 1):
        print(i)


def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("sum of all no. :", total)


def is_prime(n):
    """
    Fixed version of original broken Prime() function:
    - 'print prime' (Python 2 syntax) removed
    - undefined 'prime' variable removed
    - function now correctly returns True/False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# ---------------- LOCAL VARIABLE ----------------
def display_local():
    x = 10
    print(x)
    # print(x) outside this function -> NameError, x is local


# ---------------- GLOBAL VARIABLE ----------------
g_x = 0  # global


def show_global():
    print(g_x)  # reads global since no local x defined


def shadow_global():
    x = 3  # local, shadows global, doesn't affect g_x
    print(x)


def modify_global():
    global g_x
    g_x = 10
    print(g_x)


# ---------------- NONLOCAL VARIABLE ----------------
def show_outer():
    x = 10

    def display_inner():
        print(x)  # reads outer x (closure)

    display_inner()


def show_outer_nonlocal():
    x = 10

    def display_inner():
        nonlocal x  # outer x ko local ki tarah use karega, modify bhi kar sakta hai
        x = x + 5
        print(x)

    display_inner()


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    hello()
    print(add_return(5, 7))

    print(print_1_to_10())
    numeric_pyramid(5)
    print(fibonacci(5))

    print(add3(1, 2, 3))
    print(fun_default(12, 12))

    print(sum_of_lists([1, 2, 3], [4, 5, 6]))
    show_kwargs(x=12, y=23, z=45, v=23)
    explore_kwargs(a=1, b=2)

    fun_combined(10, 20, 30, 40, 50, p="naveen", r=2, s=3, t=4)

    natural_no(5)
    natural_sum(5)
    print(is_prime(7))

    display_local()
    show_global()
    modify_global()

    show_outer()
    show_outer_nonlocal()