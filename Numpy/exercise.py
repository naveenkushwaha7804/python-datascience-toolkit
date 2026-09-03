import numpy as np

b = np.array([10, 20, 30, 40, 50])
a=b.astype(int)
# Mean=(10+20+30+40+50)/5 = 30
print(np.mean(b))
# Median=बीच का number = 30
print(np.median(a))
# std का मतलब Standard Deviation (मानक विचलन) है।
# यह बताता है कि data average से कितना फैलाव (spread) रखता है।
print(np.std(a)) #standarf deviTION
# var का मतलब Variance (विचरण) है।
# Variance=(StandardDeviation)2
# यह standard deviation का square होता है।
print(np.var(a))#Varience
print(np.power(a, 2))



b = np.array([[1,2,3],
              [4,5,6]])
print(np.mean(b, axis=0))  # ((1 + 4) / 2 = 2.5)column average
print(np.mean(b, axis=1))  # ((1 + 2 + 3) / 3 = 2) row average

a = np.array([[1,2,3,4]])
print(a.flatten())
print(b.ravel()) #flatten() and ravel() का काम है multi
# -dimensional array को 1D array में बदलना।

a.resize(2,2)#resize() का काम है array का 
# shape (rows और columns) बदलना।
print(a)

b = np.array([[1,2],
              [3,4]])

# # print(b.flatten())

print(np.transpose(b)) #transpose() rows को columns
# में और columns को rows में बदल देता है।

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate((a,b)))#concatenate() का मतलब 
# होता है arrays को जोड़ना (merge करना)।

x = np.array([[1,2],
              [3,4]])

y = np.array([[5,6],
              [7,8]])

print(np.concatenate((x,y), axis=0))  # row wise concatination
print(np.concatenate((x,y), axis=1))  # column wise concatination




# a=np.zeros((2,3))
# b=a.astype(int)
# print(b)



