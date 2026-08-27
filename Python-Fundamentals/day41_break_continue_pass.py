'''
- continue -> skip current iteration, loop agli iteration pe chala jaata hai
- break    -> current loop ko terminate kar deta hai
- pass     -> current block ko skip karta hai (kuch nahi karta, placeholder)
'''


def continue_demo(n):
    """
    continue example (while loop).
    Bug fix: original code mein i+=1 continue se pehle nahi tha,
    isliye i==5 par infinite loop ban jaata tha. Yahan increment
    continue se pehle kar diya hai.
    """
    i = 1
    while i < n:
        i += 1  # increment pehle, taaki continue infinite loop na bane
        if i == 5:
            continue  # 5 skip ho jaayega, aage ka print nahi chalega
        print(i)


def pass_demo_while(n):
    """pass example (while loop) - 5 ko print nahi karega, bas skip (pass) karega."""
    i = 1
    while i < n:
        if i == 5:
            pass  # kuch nahi hoga, but loop aage badhega
        else:
            print(i)
        i += 1


def pass_demo_for(n):
    """pass example (for loop) - 5 ko print nahi karega."""
    for i in range(1, n + 1):
        if i == 5:
            pass
        else:
            print(i)


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    n = int(input("Enter a value: "))
    pass_demo_for(n)

    # Uncomment to try other demos:
    # continue_demo(n)
    # pass_demo_while(n)