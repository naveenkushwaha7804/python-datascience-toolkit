def get_numbers():
    """Take n numbers as input from user and return as a list."""
    count = int(input("Enter numbers: "))
    l = []
    for i in range(1, count + 1):
        value = int(input(f"Enter {i} number: "))
        l.append(value)
    return l


def add_numbers():
    l = get_numbers()
    total = sum(l)
    print(f'Addition of {l} is {total}')


def sub_numbers():
    l = get_numbers()
    result = l[0]
    for num in l[1:]:
        result -= num
    print(f'Subtraction of {l} is {result}')


def multiply_numbers():
    l = get_numbers()
    result = 1
    for num in l:
        result *= num
    print(f'Multiplication of {l} is {result}')



def divide_numbers():
    l = get_numbers()
    result = l[0]
    for num in l[1:]:
        if num == 0:
            print("Error: division by zero, skipping this value")
            continue
        result /= num
    print(f'Division of {l} is {result}')


def calculator():
    while True:
        print(" 1. Add\n 2. Sub\n 3. Div\n 4. Multi\n 5. Exit")
        choice = int(input("Enter a value from above: "))

        if choice == 1:
            add_numbers()
        elif choice == 2:
            sub_numbers()
        elif choice == 3:
            divide_numbers()
        elif choice == 4:
            multiply_numbers()
        elif choice == 5:
            break
        else:
            print("Please enter a valid choice:")


if __name__ == "__main__":
    calculator()