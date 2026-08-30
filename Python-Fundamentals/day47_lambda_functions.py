#         Syntex
# x=lambda parameters : expresion


# x=lambda x,y,z:2*x+3*y+z
# print(x(2,3,4))

'''
 With if else 
lamda parameters: if_result if condition else_result
'''
# x=lambda x,y:x if x>y else y
# print(x(2,4)).


'''
age=int(input("Enter your age :"))
y=lambda x:"you are senior " if age>60 else (" you are young"if 60> age >40 else("you are sdult " if 40>age>15 else "you are child"))
print(y(age))
'''


'''
x=int(input("Enter a number :"))
a=lambda x:"Even no." if x%2==0 else None
print(a(x))
'''


x=int(input("Enter a number :"))
a=lambda x:[i for i in range(1,x+1)]
print(a(x))


'''
x=int(input("Enter a number :"))
a=lambda x:[i for i in range(1,x+1) if i%2==0]
print(a(x))
#while loop nahi lagta isme 
'''
'''
l=[1,2,3,4,5]
print(list(map(lambda n:n**2,l)))
'''
'''
l1=[1,2,3,4]
l2=[4,5,6,7]
l3=[4,7,8,9]
print(list(map(lambda x,y,z:x+y+z,l1,l2,l3)))
'''

'''
l3=[4,7,8,9]
print(list(filter(lambda x:x if x%2==0 else None ,l3)))
# or
l3=[4,7,8,9]
print(list(filter(lambda x: x%2==0,l3)))
'''

# from functools import reduce
# l3=[4,7,8,9]
# print((reduce(lambda x,y:x if x>y else y,l3)))
# y=lambda x,r,t:2*x+4*r+t
# print(y(2,4,6))
# d=lambda x,c,v:x if c<x>v else c if x<c>v else v
# print(d(3,5,8))
