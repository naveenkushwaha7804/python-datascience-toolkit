def wishme():
    """Simple greeting function."""
    print("welcome")
    print("Naveen")


def add(a, b):
    """Print sum of two numbers."""
    print("the sum is:", a + b)


def add_sub(a, b):
    """Return sum and difference of two numbers."""
    return a + b, a - b


def is_prime(n):
    """Check if a number is prime."""
    for i in range(2, n):
        if n % i == 0:
            return "number is not a prime number"
    return "number is a prime number"


def circle_area_circumference(r):
    """Return area and circumference of a circle for radius r."""
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference


def multiply_three(a, b, c):
    """Multiply three numbers."""
    return a * b * c


def add_three(a, b, c):
    """Add three numbers."""
    return a + b + c


def fun_name(**kwargs):
    """Demonstrate **kwargs - collects keyword args into a dict."""
    print(kwargs)
    print(type(kwargs))


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    print("nab")
    wishme()
    add(1, 3)

    s, d = add_sub(1, 3)
    print(f"sum={s}, diff={d}")

    result = is_prime(int(input("enter a no.: ")))
    print(result)

    a, c = circle_area_circumference(float(input("enter radius: ")))
    print("the area is:", a)
    print("the circumference is:", c)

    print(add_three(2, 3, 4))

    fun_name(x=12, y=23, z=45, v=23)