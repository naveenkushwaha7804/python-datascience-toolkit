# Syntex
'''
iterable1
iterable2
iterable3
def fun_name(parameter1,parameter2,parameter3):
    |
    |
    |
    |
    |
res=map(fun_name,iterable1,iterable2,iterable3)
print(list(res))
map(function,iterable)
'''

# l1=[1,2,3,4]
# l2=[6,7,8,9]
# l3=[1,3,4,8]
# def add(x,y,z):
#     return x+y+z
# res=map(add,eval(input("enter a list")),eval(input("enter a list")),eval(input("enter a list")))
# print(list(res))

def add(x):
        return x**2

res=map(add,eval(input("enter a list")))
print(list(res))