#  Represented b y "@"
# Defination = yah ek higher order function hai yah argument
#  me function lega or return v ek function karega

'''
def decore(fun_name):
    def inner():
        print("Hello World")
    return inner
x=decore(10)
print(x)
x()
'''

'''
def decore(fun):
    def inner():
        fun()
    return inner
def add( ):
    print("Hello")
res=decore(add)
res()
'''
'''
def decore(fun):
    def inner(p,q):
        p=p+5
        q=q*2
        fun(p,q)
    return inner
def add(x,y):
    print(x+y)
res=decore(add)
res(10,20)
'''
'''
def decore(fun):
    def inner(p,q):
        p=p+5
        q=q*2
        fun(p,q)
    return inner
@decore
def add(x,y):
    print(x+y)
add(10,20)
'''

'''
def first(fun):
    def inner():
        print("Welcome")
    return inner
@first
def great():
    print("hello")
great()
'''
'''
def decore(fun):
    def inner(n):
        for i in range(1,n+1):
            print(2*i-1,end=" ,")
    return inner
@decore
def even(n):
    for i in range(1,n+1):
        print(2*i,end=",")
n=int(input("Enter a value :"))
even(n)
'''