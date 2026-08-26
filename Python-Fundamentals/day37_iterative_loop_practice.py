def vowel_consonant_counter(s):
    """Count vowels and consonants in a string."""
    v = c = 0
    if s.isalpha():
        for i in s:
            if i.lower() in ('a', 'e', 'i', 'o', 'u'):
                v += 1
            else:
                c += 1
        print('vowel:', v)
        print('conson:', c)
    else:
        print("please enter only alphabet")


def print_natural_numbers(n):
    """Print 1 to n, comma-separated."""
    for i in range(1, n + 1):
        print(i, end=',' if i < n else '\n')


def print_natural_sum(n):
    """Print 1+2+...+n = sum."""
    total = 0
    for i in range(1, n + 1):
        total += i
        print(i, end='+' if i < n else '=')
    print(total)


def print_even_numbers(n):
    """Print first n even numbers."""
    for i in range(1, n + 1):
        print(2 * i, end=',' if i < n else '\n')


def print_even_sum(n):
    """Print sum of first n even numbers."""
    total = 0
    for i in range(1, n + 1):
        total += 2 * i
        print(2 * i, end=',' if i < n else '=')
    print(total)


def print_odd_sum(n):
    """Print sum of first n odd numbers."""
    total = 0
    for i in range(1, n + 1):
        total += (2 * i - 1)
        print(2 * i - 1, end=',' if i < n else '=')
    print(total)


def print_even_range(n):
    """Print even numbers from 2 to n."""
    for i in range(2, n + 1, 2):
        print(i, end=' ')
    print()


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    n = 12
    print_even_range(n)

    # Uncomment to try other exercises:
    # vowel_consonant_counter(input("Enter any string: "))
    # print_natural_numbers(int(input("Enter value: ")))
    # print_natural_sum(int(input("Enter value: ")))
    # print_even_numbers(int(input("Enter value: ")))
    # print_even_sum(int(input("Enter value: ")))
    # print_odd_sum(int(input("Enter value: ")))