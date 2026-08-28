def print_n_natural(n):
    """Print 1 to n."""
    for i in range(1, n + 1):
        print(i)


def sum_n_natural(n):
    """Print 1 to n and their sum."""
    total = 0
    for i in range(1, n + 1):
        total += i
        print(i)
    print(total)


def print_n_even(n):
    """
    Print first n even numbers.
    Fixed: original had range(1,) with no stop value and wrong logic.
    """
    for i in range(1, n + 1):
        print(2 * i)


def swap_first_last_char(s):
    """
    Swap first and last character of a string.
    Fixed: newstring was only defined inside 'if len(s)>1', causing
    NameError on short strings. Now handles all cases.
    """
    if len(s) > 1:
        chars = list(s)
        chars[0], chars[-1] = chars[-1], chars[0]
        return "".join(chars)
    return s


def word_frequency(sentence):
    """
    Count frequency of each word in a sentence.
    Fixed: original code had garbled/broken syntax mixing import and input.
    """
    from collections import Counter
    return Counter(sentence.split())


def is_prime(n):
    """Check primality using for-else."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def right_triangle(n):
    """Print right-angle number triangle: 1 / 1 2 / 1 2 3 ..."""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def remove_min(t):
    """Remove the minimum value from a tuple (via list conversion) and return new min."""
    lst = list(t)
    lst.remove(min(lst))
    return min(lst)


def calculate_hra_da(salary):
    """Calculate HRA and DA based on salary slabs."""
    if salary <= 0:
        print("invalid input")
        return
    if salary <= 10000:
        hra, da = salary * 0.2, salary * 0.8
    elif salary <= 20000:
        hra, da = salary * 0.25, salary * 0.9
    else:
        hra, da = salary * 0.3, salary * 0.95
    print(f"HRA = {hra}", f"your DA is {da}")


def multiply_first_last_digit(no):
    """Multiply first and last digit of a number."""
    s = str(no)
    return int(s[0]) * int(s[-1])


def factorial(n):
    """
    Calculate factorial using simple iteration.
    Fixed: original used a broken class with super(1,n), which is invalid
    usage of super() (meant for parent-class access, not computation).
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def split_first_n_words(text, n):
    """Split text into first n words + remainder."""
    return text.split(" ", n)


def sum_of_digits(no_str):
    """Sum of digits of a number (given as string input)."""
    return sum(int(ch) for ch in no_str)


def reverse_string(s):
    """Reverse a string."""
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    a = input("enter a string: ")
    print(reverse_string(a))

    # Uncomment to try other exercises:
    # print_n_natural(int(input("enter a no. :")))
    # sum_n_natural(int(input("enter a no. :")))
    # print_n_even(int(input("enter a no.")))
    # print(swap_first_last_char(input("enter a string :")))
    # print(word_frequency(input("enter any sentence :")))
    # print(is_prime(int(input("enter a no :"))))
    # right_triangle(int(input("enter a no :")))
    # print(remove_min((1, 2, 3, 4, 5, 6, 67, 8)))
    # calculate_hra_da(int(input("Enter your basic salary :")))
    # print(multiply_first_last_digit(int(input("enter a no. :"))))
    # print(factorial(int(input("enter a no :"))))
    # print(split_first_n_words("one two three four five six seven eight", 3))
    # print(sum_of_digits(input("enter a no.")))