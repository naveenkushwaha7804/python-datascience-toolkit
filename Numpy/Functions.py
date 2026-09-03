import numpy as np

#          copy()

# A=np.array([1,2,3,4,5,6])
# print(A)
# B=A.copy()
# B[0]=200
# print(B)
# print(A)
# # copy() me changes ke sath original array me changes nahi honge

# #          view()

# A=np.array([1,2,3,4,5,6])
# print(A)
# B=A.view()
# B[0]=200
# print(B)
# print(A)
# View() me  changes ke sath original me b changes honge

#          append()

# A=np.array([1,2,3,4,5,6])
# print(A)
# B=A.view()
# # B[0]=345
# B=np.append(B,345)
# print(B)
# print(A) # yaha pr append ke sath element jud gya hai to 
# # new memory ban gai hai isliye original array me changes nahi aaye 

#          add() 

# A=np.array([1,2,3,4,5,6])
# # print(A)
# B=A.view()
# # B=B+1 #Same add function work karta hai
# B=np.add(B,2)
# # B=np.subtract(B,3)
# # B=np.multiply(B,5)
# # # # every operation will be working
# print(B)
# print(A)
#  Every element will updated with addition operation

#          insert()

# A=np.array([1,2,3,4,5,6])
# print(A)
# B=A.copy()
# # B[0]=200 Same as
# B=np.insert(A,5,455)
# print(B)

#          random.choice()

A=np.random.choice([1,2,3,4,5,6],size=[2,3,2])
print(A)
# B=np.random.choice([1,2,3,4,5,6],size=[2,3])
# C=np.random.choice([1,2,3,4,5,6],size=[2])
# print(A)
# print(B)
# print(C)
# #  Randomli in diye huye element se size le 
# # according  array generate karke return karega

# #          sort()
# A=np.array([1,2,34,12,65,34])
# A=np.sort(A)
# print(A)
# # #  for decending order
# B=np.sort(A)[::-1]
# print(B)

# #          argsort()
# sort karne ke baad values ki index return karta hai
# A=np.array([1,2,34,12,65,34])
# B=np.argsort(A)
# print(np.argmax(A))
# print(np.argmin(A))
# # print(np.sort(A))
# # print(B)

# # #          array_split()

# # # 1D
# # A=np.array([1,2,34,12,65,32,32])
# # B=np.array_split(A,2)
# # print(B)
# # print(B[0])
# # print(B[1])

# # # 2D
# # D2=np.array([[1,2,3,4],[5,6,7,8]])
# # D22=np.array_split(D2,2)
# # C=D22[0]
# # print(D22)
# # print(C)
# # print(D22[0])

# # #          d_stack() / Depth Stack

# T1=np.array([[1,3,5,6,2,4,],[23,12,34,4,34,56]])
# print(T1)
# T2=np.dstack(T1)
# print(T2)
# # print(T2.ndim)

# # #          v_stack() / Vertical Stack / do array ko jodta hhai

# T1=np.array([1,3,5,6,2,4,])
# print(T1)
# T3=np.vstack(T1)
# print(T3)
# print(T3.ndim)
# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# c=np.vstack((a,b))
# print(c)

# # yadi hame column ko row ya row ko column me convert karna hai to iska use karenge
# D2=np.array([[1,2,3,4],[5,6,7,8],[23,2312,12,1]])
# print(D2)
# # D3=np.dstack(D2)
# # print(D3)

# # #            Transpose()
# A=np.array([[1,2,3,4,5],[6,7,8,9,6]])
# print(A)                                               
# Z=np.transpose(A)
# print(Z)

# # #            Delete()/1D

# A=np.array([1,2,3,4,5,6])
# # B=A[A!=5] # [this is maskingg ]
# print(B)
# B=np.delete(A,2)
# print(B)  
# B=np.delete(A,0)
# print(B)
# C=np.delete(A,np.where(A==6))
# print(C)

# # #            Delete()/2D
# A=np.array([[1,2,3,4],[5,6,7,8]])
# B=np.delete(A,4)
# print(B)

# #        Work
# A=np.arange(0,12).reshape(3,4)
# print(A)
# A=np.delete(A,[1,3],axis=1)
# print(A)

# #        changes nahi honge

# X=np.array([1,2,3,4,5,6])
# X.setflags(write=False)
# Y=np.insert(X,0,213)
# Y=np.append(X,213)
# # X[0]=34  Nahihoga changes
# print(Y)

# B=np.array([1,2,3,4,4])
# C=np.array([4,5,6,7,8])
# print(np.intersect1d(B,C))
# print(np.union1d(B,C))