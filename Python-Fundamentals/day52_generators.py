'''
x=range(1,100)
print(list(x))
# print(id(list(x)))
for i in x:
    if i==1 or i==2:
        print(i)
print("Hello")
print("welcome")
for i  in x:
    if i==3 or i==4:
        print(i)
'''
def naturalno(n):
    i=1
    while i<=n:
        yield i # yield position hold kaarta hai phir ange ki value deta haai
        i=i+1
x=10
res=naturalno(x)
print(res)
# for i in res:
#     print(i)
# print(next(res))
# print(next(res))
# print("hello")
# print(next(res))
for i in range(2):
    print(next(res))
print("hii")
for i in  range(4):
    print(next(res))
for i in  range(7):
    try:
        print(next(res))
    except StopIteration:
        print("ALl elements are iterated i.e Collection is empty")
        break
  