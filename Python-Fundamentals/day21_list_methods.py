# LIST METHOD

l = [10, 20, 30, 'python', 40, 'java', 50]

# methods

# l.append()   # list ke last me ek single element add karne ke liye
# l.copy()     # create new object with same elements
# l.clear()    # clear all elements from list
# l.index()    # find out order / location of any element
# l.count()    # find frequency of any object
# l.pop()      # remove index targeted element, by default it removes -1 index element
# l.remove()   # remove targeted element
# l.extend()   # add multiple elements at last position
# l.sort()     # to arrange all elements in ascending order
# l.reverse()  # to reverse all given elements
# l.insert()   # add element in targeted position


# n = eval(input('Enter an element'))

# print(l.append(n))
# print(l)

# print(l.extend(n))

# print(l.insert(2, 'g'))  # input alag se nahi lenge


# l1 = l.copy()
# print(l1)
# print(id(l))
# print(id(l1))


# print(l.clear())
# print(l)


# del l  # for delete from memory
# print(l)


# print(l.pop(2))
# print(l.pop())
# print(l)


# print(l.pop())
# print(l)


# print(l.remove('python'))
# print(l)


# print(l.index('python'))
# print(l)


# print(l.count('python'))
# print(l)


# for only homogeneous list
l2 = [10, 20, 30, 40, 2]

print(l2.sort())
print(l2.sort(reverse=True))  # for reverse
print(l2)


# HW: list operators