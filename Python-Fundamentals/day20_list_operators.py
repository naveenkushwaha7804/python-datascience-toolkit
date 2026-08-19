    # OPERATORS ON LIST
# 1.AIRTHMETIC OPERATOR (+,-,,/,%.//,*)

# l1=[10,4,8,'naveen',7]
# l2=[9,4,'java',3,8]
# print(l1+l2)
# sum(+) is work as concatination 

# UNSUPPORTED (-) OPERATOR
l1=[10,4,'python',8,4]
l2=[9,4'java',8,0]
print(l1-l2)

# SUPPORTED (*) OPERATOR
# l1=[10,4,'python',8,4]
# l2=[9,4,'java',9]
# print(l1*2)
# print(l2*5)
# (*) Repetation, multiply are applied on list

# (-,/,%.//,) operatores are not supported on list

print(l1-l2)
print(l1/l2)
print(l1%l2)
print(l1//l2)
print(l1**l2)

# 3.COMPARISION OPERATOR(==,!=,>,>=,<,<=)

l1=[10,30,80,64]
l2=[43,76,84,8]
print(l1==l2)
print(l1!=l2)
print(l1>l2)
print(l1>=l2)
print(l1<l2)
print(l1<=l2)

# 4.LOGICAL OPERATOR

x=[]
y=[]
print(x and y)

x=[]
y=[6,4,3]
print(x and y)

x=[4,2,1]
y=[]
print(x and y)

x=[4,3,2]
y=[9,4,2]
print(x and y)
print(y and x)


x=[]
y=[]
print(x or y)

x=[]
y=[6,4,3]
print(x or y)

x=[4,2,1]
y=[]
print(x or y)

x=[4,3,2]
y=[9,4,2]
print(x or y)

l=[]
print(not(bool(l)))

# 5.MEMBERSHIP OPERATOR

l=[30,60,98]
print(06 in l)
print(30 in l)
print(89 in l)
print(60 in l)

# 6.IDENTITY OPERATOR
l1=[30,60,98]
l2=[4,8,7]
print(l1 is l2)
print(l1 is not l2)
print(l2==l1)