def square(n):
    """Print n x n square of stars."""
    for i in range(1, n + 1):
        print('*' * n)


def triangle_left_aligned(n):
    """Right-angle triangle, spaced stars."""
    for i in range(1, n + 1):
        print('* ' * i)


def triangle_right_aligned(n):
    """Right-angle triangle, right-aligned."""
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)


def pyramid(n):
    """Centered pyramid, spaced stars."""
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)


def inverted_triangle(n):
    """Upside-down right-angle triangle."""
    for i in range(0, n):
        print(' ' * i + '*' * (n - i))


def inverted_pyramid(n):
    """Upside-down pyramid, spaced stars."""
    for i in range(0, n):
        print(' ' * i + '* ' * (n - i))


def diamond(n):
    """Full diamond: pyramid + inverted pyramid."""
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)


def alphabet_grid(n):
    """Print n-1 rows, each with A to (A+n-1)."""
    i = 1
    while i < n:
        ch = 'A'
        j = 1
        while j <= n:
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)
            j += 1
        print()
        i += 1


def numeric_odd_pattern(n):
    """Row b has b odd numbers, restarting each row: 1 / 1 3 / 1 3 5 ..."""
    for b in range(1, n + 1):
        for i in range(1, b + 1):
            print(2 * i - 1, end=' ')  # even: 2*i | normal: i
        print()


def numeric_continuous_pattern(n):
    """Row b has b numbers, continuing count across rows."""
    y = 1
    for b in range(1, n + 1):
        for i in range(1, b + 1):
            print(y, end=' ')  # even: 2*y | odd: 2*y-1
            y += 1
        print()


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    n = int(input("Enter rows: "))
    square(n)

    # Uncomment to try other patterns:
    # triangle_right_aligned(n)
    # pyramid(n)
    # triangle_left_aligned(n)
    # inverted_triangle(n)
    # inverted_pyramid(n)
    # diamond(n)
    # alphabet_grid(n)
    # numeric_odd_pattern(n)
    # numeric_continuous_pattern(n)