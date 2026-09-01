# iterable = likst,tuple,string,dict
l=[1,2,34,23,4,5]
x=iter(l)  # generate karega ange ke elements
# print(x)  Object ban jayega bs
# for i in range(2):
#     print(l[i])
# print("hello")
# for i in range(3):
#     print(l[i])
for i in range(39): # yah yaha error nahi dega generate karta jayega
    print(next(x))