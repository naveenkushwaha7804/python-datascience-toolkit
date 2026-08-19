# List Creation
l = [10, 20, 'python', 10, 20]
print("Original List:", l)
print("Type:", type(l))

# Length
print("Length:", len(l))

# Indexing
print("First Element:", l[0])
print("Last Element:", l[-1])

# Slicing
print("First Three Elements:", l[:3])
print("Last Two Elements:", l[-2:])

# Adding Elements
l.append(30)
print("After append:", l)

# Inserting Element
l.insert(1, 15)
print("After insert:", l)

# Removing Element
l.remove(10)
print("After remove:", l)

# Updating Element
l[0] = 100
print("After update:", l)

# Counting Elements
print("Count of 20:", l.count(20))

# Finding Index
print("Index of Python:", l.index('python'))

# Sorting Numeric List
numbers = [50, 10, 40, 20, 30]
print("Before Sorting:", numbers)

numbers.sort()
print("Ascending Order:", numbers)

numbers.reverse()
print("Descending Order:", numbers)

# Membership Check
print("Is 20 present?", 20 in numbers)
print("Is 100 present?", 100 in numbers)