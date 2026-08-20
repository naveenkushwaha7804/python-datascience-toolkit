# ==================== SET ====================

# Set is a collection of unique elements.
# Set is represented using {} with comma-separated values.

my_set = {10, 10, 30, 'python', 'java'}

print(my_set)
print(type(my_set))


# ==================== EMPTY SET ====================

# An empty set is created using set().
# {} creates an empty dictionary, not an empty set.

my_set1 = set()

print(my_set1)
print(type(my_set1))


# ==================== FROZEN SET ====================

# Frozenset is an immutable version of a set.
# Once created, its elements cannot be changed.

my_set3 = {10, 10, 30, 'python', 'java'}

fs = frozenset(my_set3)

print(fs)
print(type(fs))


# ==================== BOOLEAN ====================

# Boolean data type has two values: True and False.

x = True
y = False

print(x, y)
print(type(x), type(y))


# ==================== NONE ====================

# None represents the absence of a value.

z = None

print(z)
print(type(z))


# ==================== OBJECT NATURE ====================

# Numeric types are immutable.

x1 = 4
y1 = 4

print(id(x1), id(y1), type(x1))


# Float is immutable.

x2 = 4.3
y2 = 4.3

print(id(x2), id(y2), type(x2))


# Complex is immutable.

x3 = 7 + 3j
y3 = 7 + 3j

print(id(x3), id(y3), type(x3))


# Tuple is immutable.

t = ('ele1', 'ele2', 'ele3')
t2 = ('ele1', 'ele2', 'ele3')

print(id(t), id(t2), type(t))


# Dictionary is mutable.

d = {'name': 'naveen', 'age': 20}
d1 = {'name': 'naveen', 'age': 20}

print(id(d), id(d1), type(d))


# List is mutable.

l = [1, 2, 3, 4, 5, 6]
l1 = [1, 2, 3, 4, 5, 6]

print(id(l), id(l1), type(l))


# ==================== IMMUTABLE DATA TYPES ====================

# 1. Integer
# 2. Float
# 3. Complex
# 4. String
# 5. Boolean
# 6. Tuple
# 7. Frozenset
# 8. None


# ==================== MUTABLE DATA TYPES ====================

# 1. List       -> CRUD operations
# 2. Dictionary -> CRUD operations
# 3. Set        -> CRUD operations