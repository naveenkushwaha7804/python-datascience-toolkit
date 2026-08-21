                          #SET() MUTABLE

# 1 - collections of unique elements
# 2 - represented by {} with comma (,) seperated elements
# 3 - unordered collection 
# 4 - indexing not supported
# 5 - slicing not supported
# 6 - mutable in nature
#hacing technique se order change karta hai

my_set={10,20,'naveen','bansal','java'}

print(my_set)

            # inbuilt function
print(len(my_set))
print(type(my_set))
print(id(my_set))
# print(max(d)) only for homogenious
# print(min(d)) only for homogenious
my_set2={10,20,40,50}
print(max(my_set2))
print(min(my_set2))

                      #METHODS

# 1 - that required more than 1 set
# 1 - that required more than 1 set

# 1- union ()
# 2- intersection()
# 3- difference()
# 4- symetric-difference() #opposite of intersection
# 5- intersection-update()
# 6- difference-update() 
# 7- symetric-difference-update()
# 8- issubset()
# 9- issuperset()
# 10- isdisjoint()

s1,s2={1,2,3,4,5},{4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# s1.intersection_update(s2)# s1 ko update kr dega or usme intersection bale element daal dega
# print(s1)
# print(s2)

# s1.difference_update(s2) # intersection bale elements hata dega
# print(s1)
# print(s2)

# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)


s3,s4={1,2,3,4,5,6,7,8},{6,7,8}
#subset hai ya nahi batayega
print(s4.issubset(s3)) 
print(s3.issuperset(s4))
print(s3.issubset(s4)) 
print(s4.issuperset(s3))

print(s1.isdisjoint(s2))  # join hai yaa nahi yah batata hai
s5={1,2,3,4,'python','naveen'}

s6=s5.copy()
print(s6)

# s5.update({7,8,9,22,11})
# print(s5)    #unique elements ko add kareAGA

# s5.discard('nav') #perticular element ko remove karne ke liye  agar element naahi hoga tab b error nahi dega 
# print(s5)

# s9=s5.clear()
# print(s9)

# s5.pop() #rendom element remove karne ke liye
# print(s5)

# s5.remove('naveen') #perticular element ko remove karne ke liye  agar element naahi hoga to error dega
# print(s5)

# s5.add('php')
# print(s5)