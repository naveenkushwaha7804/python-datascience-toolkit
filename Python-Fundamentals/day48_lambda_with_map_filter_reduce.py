# lambda
# a function with no name is called lambda function
# anonmys function---> meaning lambda

# syntax

'''x=lamda parameter:expression
   x=(argument)

  As per documentation
       lambda variable:expression
'''

# It resolve single expression
# x=lambda x,y,z:x+y+z
# print(x(1,2,3))

# x=lambda x,y:x if x>y else y
# print(x(5,10))

# x=lambda age:'child' if age>=0 and age<=17 else 'adult' if 18>age<=59 else 'senior' if 59>=age else 'invalid age'
# print(x(int(input("enter age:"))))


# even or not:-
# x=lambda n: 'even' if n%2==0 else None
# n=int(input("enter number:"))
# print(x(n))


# square
# x=lambda n:n**2
# n=2
# print(x(n))

# to get collection
# n=int(input("enter any no.:"))
# x=lambda n:[i for i in range(1,n+1)]
# print(x(n))


# up to 10 even number
# x=lambda n:[i for i in range(1,n+1) if i%2==0]
# n=int(input("enter a number"))
# print(x(n))


# map with lambda
# l=[1,2,3,4,5]
# print(list(map(lambda n:n**2,l)))


# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=[3,4,5,6]
# print(list(map(lambda x,y,z:x+y+z,l1,l2,l3)))



# l=[1,2,3,4,5,6,7]
# print(list(filter(lambda l:l%2==0,l)))

import functools 
l=[1,2,3,4,5,6,7]
print((functools.reduce(lambda l,l1:l+l1,l)))