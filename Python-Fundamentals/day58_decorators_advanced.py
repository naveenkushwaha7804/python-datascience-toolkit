# DECORATOR (@)
# A decorator is a higher-order function that modifies the behavior
# of another function without changing its original code.
# It takes a function as an argument and returns a function.

def decore(fun):
    def inner(x):
        for i in range(1, x + 1):
            print(3 * i)
    return inner


@decore
def numbers(n):
    for i in range(1, n + 1):
        print(1 / i)


n = int(input("Enter any value: "))
numbers(n)