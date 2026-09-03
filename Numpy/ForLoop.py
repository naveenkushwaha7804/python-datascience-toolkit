import numpy as np

# #       1D
# # np.arange(start, stop, step)

# # d=np.arange(1,10,2)
# # print(d)
# # a=d.reshape(1,5)#reshape() का काम है array का shape बदलना।
# # print(a)
# # for i in range(len(a)):
# #     print(a[i],i)

# # | Function    | काम                         |
# # | ----------- | --------------------------- |
# # | `arange()`  | range में array बनाता है    |
# # | `reshape()` | array का shape बदलता है     |
# # | `len()`     | rows की संख्या बताता है     |
# # | `range()`   | loop के लिए numbers देता है |

# # # Indexed bassed

# # ==============================

# # 1D for loop value bassed
# # d=np.arange(1,10,2)
# # print(d)
# # for i in d:
# #     print(i)
# # # # Value Bassed

# # # IN NUMPY
# # for i in np.nditer(d):
# #     print(i)
# # # Value + Indexed Basses
# # for i in np.ndenumerate(d):
# #     print(i)

# # =================================

# # 2D (for loop value bassed)

# d2=np.array([[1,2,3],[5,6,7]])
# d2
# # for r in d2:
# #     for c in r:
# #         print(c)
# # #  # IN NUMPY
# for i in np.nditer(d2):
#     print(i)
    
# # # Value + Indexed Basses
# for i in np.ndenumerate(d2):
#     print(i)

# ===============================

# 3D (for loop value bassed)
d3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(d3)
for t in d3:
    for r in t:
        for c in r:
            print(c)
# #  # IN NUMPY
for i in np.nditer(d3):
    print(i)
for i in np.ndenumerate(d3):
        print(i)

