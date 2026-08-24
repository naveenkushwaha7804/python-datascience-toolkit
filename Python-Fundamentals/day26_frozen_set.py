# FROZEN SET 
 
''' 
= Collection of unique elements 
= Represented by frozenset({}) with comma (,) separated elements 
= Unordered collection 
= Indexing not supported 
= Slicing not supported 
= Immutable in nature 
''' 
 
s = 'python' 
l = [10, 20, 30, 'python'] 
t = [1, 2, 3, 4, 'java'] 
 
fs1 = frozenset(s) 
print(fs1, type(fs1)) 
 
''' 
fs2 = frozenset(l) 
print(fs2, type(fs2)) 
 
fs3 = frozenset(t) 
print(fs3, type(fs3)) 
''' 
 
s1 = [10, 20, 30, 40] 
s2 = frozenset(s1) 
 
 
# INBUILT FUNCTIONS 
 
print(len(s2)) 
print(type(s2)) 
print(id(s2)) 
 
# print(max(s2))  # Only for homogeneous elements 
# print(min(s2))  # Only for homogeneous elements 
 
 
# METHODS 
 
fs1 = frozenset({1, 2, 3, 4, 5}) 
fs2 = frozenset({4, 5, 6, 7, 8, 9}) 
 
print(fs1.union(fs2)) 
print(fs1.intersection(fs2)) 
print(fs1.difference(fs2)) 
print(fs1.symmetric_difference(fs2)) 
print(fs1.issubset(fs2)) 
print(fs1.issuperset(fs2)) 
print(fs1.isdisjoint(fs2))