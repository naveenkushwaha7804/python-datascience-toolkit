'''
Basic while loop structure:
initializing point
while (terminating condition):
    while-body
    increment/decrement
'''


def print_n_natural(n):
    """Print 1 to n using while loop."""
    i = 1
    while i <= n:
        print(i)
        i += 1


def count_digits(n):
    """Count total digits in a number."""
    td = 0
    while n > 0:
        td += 1
        n = n // 10
    return td


def is_armstrong(n):
    """
    Check if a number is an Armstrong number.
    Armstrong number: sum of (each digit ^ total_digits) == original number.
    """
    original = n

    total_digits = count_digits(n)

    m = original
    digit_sum = 0
    while m > 0:
        ld = m % 10
        digit_sum += ld ** total_digits
        m = m // 10

    if original == digit_sum:
        print(f'given no. {original} is armstrong')
    else:
        print(f'given no. {original} is not armstrong')


def find_factors(n):
    """Find and return all factors of n (excluding n itself, starting from 2)."""
    i = 2
    factors = []
    while i < n:
        if n % i == 0:
            factors.append(i)
        i += 1
    print(f"factor of given no.{n} is {factors}")
    return factors


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    # print_n_natural(10)

    n = int(input("enter a value = "))

    is_armstrong(n)

    find_factors(45)