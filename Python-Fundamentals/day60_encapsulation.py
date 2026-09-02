#   PUBLIC VARIABLE


class A:
    x=10
    def show(self):
        print("from class A")
        print(A.x)
class B(A):
    pass
obj=B()
print(obj.x)
obj.show()
print(A.x)
A.show(10)
print(dir(A))


#   PRotected VARIABLE
#  PYTHON not supported

'''
class A:
    _x=10
    def _show(self):
        print("from class A")
        print(A.x)
class B(A):
    pass
obj=B()
print(obj._x)
obj._show()
print(A._x)
A._show(10)
'''

#   PRIVATE VARIABLE


class A:
    __x=10
    def __show(self):
        print("from class A")
        print(A.__x)
class B(A):
    pass
obj=B()
# print(obj.__x)
# obj.__show()
# print(A.__x)
# A.__show(10)
print(dir(A))
print(A._A__x)
# __class_name__variable/method
# support nahi karega
