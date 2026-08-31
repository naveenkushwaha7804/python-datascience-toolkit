# # Generator
# jayada control formate me generate krke deta helpyeild ek value lekar bahar aata he
# next dusri ka wait krta he 
# x=range(1,100)
# print(list(x))
# print(id(list(x)))



# def natural(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1
# x=10
# res=natural(x)
# print(res)
# for i in res:
#     print(i)
# print(next(res))
# print(next(res))
# print("hello")
# print(next(res))
# for _ in range(2):
#     print(next(res))
# print("Hello")
# print("Welcome")
# for _ in range(3):
#     print(next(res))


# for _ in range(5):
#     print(next(res))
# print("Hello")
# print("Welcome")
# for _ in range(10):
#     print(next(res))      # error---> StopIteration



def natural(n):
    i=1
    while i<=n:
        yield i
        i=i+1
x=20
res=natural(x)
print(res)
for _ in range(30):
    try:
       print(next(res))
    except StopIteration:
        print("all elements are iterated,i.e collection is empty")
        break



# iterable,iterator
# when we have already generate the collection but i want to control the list so we use iter in built function
# python collections are known as iterable
# list, tuple, string, dict
# l=[1,2,3,4,5]
# print(l)
# x=iter(l)
# print(x)
# # for i in x:
# #     print(i)
# for i in range(5):
#     print(next(x))
# for i in range(2):
#     print(l[i])
# print("hello")
# for i in range(2):
#     print(l[i])


 