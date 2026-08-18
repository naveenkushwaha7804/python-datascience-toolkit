# Jo method '__' se start or khatam hote hai unko magic method bolte hai
# Jo method '_' se start hote or khatam hai unko dinder method bolte hai

# typesof methods

# 1= lower()
# 2= upper()
# 3= capitalize / pehla chacracter capital kar dega
# 4= title()  /capital kar dega  sabhi word ka pehla letter 
# 5=index()  
# 6= count()
# * 7= split()
# * 8= join()
# * 9= find()
# * 10= replace()
# 11= swapcase()  /  capital ko small me small ko capital me convert kr dega
#     etc.......

s='Python'
print(s.swapcase())
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
# change nahi hoga kyuki  immutable hai
print(s)
#   indexing
print(s.index('t'))
print(s.find('a'))
print(s.find('o')) # index or hai ya nahi 
print(s.count('P')) # frequency (kitni baar aaya hai)