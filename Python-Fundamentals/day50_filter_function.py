l=[1,2,3,4,5,6,7,8,9,4,5,6,6,7]
def fun_name(parameter):
    if (parameter-1)%2==0:
        return parameter
res=filter(fun_name,l)
print(list(res))