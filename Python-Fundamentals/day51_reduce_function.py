from functools import reduce   #pehle filter ko access ke liye import karna padega


'''
l=eval(input("enter a list : "))
def max(iterable1,iterable2):
    if iterable2<iterable1:
        return iterable1
    else:
        return iterable2

res=reduce(max,l,0) # zero initial hoga or yah sum+=0 ke jese sum ke roop me kaam karega
print(res)
'''


l=eval(input("enter a list"))
def max(iterable1,iterable2):
     return iterable1+(iterable2**2) 

res=reduce(max,l,0) # zero initial hoga or yah sum+=0 ke jese sum ke roop me kaam karega
print(res)


l=eval(input("enter a list"))
def max(iterable1,iterable2):
     fact=1
     for i in range(1,iterable2+1):
          fact*=i
     return iterable1+fact #itraabale1 isliye kyuki jo value usme store hui hongi 
                            # unko b to chaahiye last no. ke factorial ke sath add hoke
res=reduce(max,l,0) # zero initial hoga or yah sum+=0 ke jese sum ke roop me kaam karega
print(res)



