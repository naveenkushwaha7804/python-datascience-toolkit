# ITERATIVE / LOOPING STATEMENT

'''
1 - While  (infinite / StopIteration)
    while else

2 - For  (finite iteration)
    for else
'''

'''
Syntax:
for i in iterable:
'''


# STRING ITERATION

'''
s = 'Python'

for i in s:
    print(i)
'''


# LIST ITERATION

'''
l = [1, 2, 3, 4, 5, 6]

for i in l:
    # i += 5
    print(i + 5)
'''


# TUPLE ITERATION

'''
t = ('python', 1, 2, 3, 4)

for i in t:
    print(i)
'''


# DICTIONARY ITERATION

'''
d = {'x': 20, 'y': 30, 'z': 50}

for i in d:
    print(i, '=', d[i])  # Extra for taking values
'''


# SET ITERATION

'''
s = {1, 2, 3, 4, 5, 6, 'python'}

for i in s:
    print(i)
'''


# FOR LOOP

# s = input("Enter your name: ")
# v = c = 0

# for i in s:
#     if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
#         v = v + 1
#     elif i == ' ':
#         pass
#     else:
#         c = c + 1

# print(f"Consonants are: {c}", f"Vowels are: {v}")


# ------------------------------------
# VOWEL AND CONSONANT COUNT

'''
s = input("Enter any string: ")
v = c = 0

s = s.replace(' ', '')  # Space ko hata dega

# print(s.isalpha())  # Alphabet hai ya nahi

if s.isalpha():
    s = s.lower()

    for i in s:
        if i in ('a', 'e', 'i', 'o', 'u'):
            v = v + 1
        else:
            c = c + 1

    print('Vowels:', v)
    print('Consonants:', c)

else:
    print('Enter only string')
'''


# ------------------------------------
# SUM OF FIRST N NATURAL NUMBERS

'''
n = int(input('Enter value: '))
sum = 0

for i in range(1, n + 1):
    sum += i

    # print(i, end=',')
    # End for taking output in one line,
    # but the last digit will also have a comma.

    if i < n:
        print(i, end='+')
    else:
        print(i, end='=')

print(sum)
'''


# ------------------------------------
# ODD / EVEN SERIES

n = int(input('Enter value: '))
sum = 0

for i in range(1, n + 1):
    sum += i

    if i < n:
        print(2 * i - 1, end=',')  # For odd: 2*i-1
    else:
        print(2 * i, end='=')      # For even: 2*i

print(sum)