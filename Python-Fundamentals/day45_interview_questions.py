import keyword
import string


def print_keywords():
    """Print all Python reserved keywords."""
    for kw in keyword.kwlist:
        print(kw)


def print_punctuations():
    """Print all punctuation characters."""
    for p in string.punctuation:
        print(p)


def print_nested_tuple(t):
    """
    Iterate through a tuple; if an element is itself iterable (like a list),
    print its inner elements too.

    Fixed issues from original code:
    - Missing loop body caused IndentationError
    - Inner loop variable reused outer tuple's name 't', which would have
      silently overwritten the outer tuple mid-iteration
    """
    for item in t:
        if isinstance(item, list):
            for inner in item:
                print(inner)
        else:
            print(item)


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    t = (1, 2, 3, [5, 6, 7])
    print_nested_tuple(t)

    # Uncomment to try other demos:
    # print_keywords()
    # print_punctuations()