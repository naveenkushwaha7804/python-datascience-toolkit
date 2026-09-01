# f=open('n5.txt','x')
'''
f=open('n5.txt','w') #  w , a , r, x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''

'''
f=open('n1.txt','a') #  w , a , r, x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''


'''
f=open('n5.txt','r') #  w , a , r, x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''

'''
f=open('n7.txt','w') #  w , a , r, x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''

# -----------------------------
'''
f=open('n5.txt','+r') #  +w , +a , +r, +x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''
'''
f=open('n9.txt','+x') #  +w , +a , +r, +x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''
'''
f=open('n10.txt','+a') #  +w , +a , +r, +x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)
'''

'''f=open('n5.txt','+w') #  +w , +a , +r, +x ,
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)'''


'''
write - 1. write()
        2- writelines()
read - 1. read()  -> read all data
       2. read\n  -> read n-bits of data
       3. readlines() -> read single-line of data
       4. read all lines of data -> read all- lines of data
Cursor movement- 1. tell() - to check cursor current position
                2. seek() - to move our cursor required position
'''

# write
'''
f=open('n1.txt','a+')
data='this is python class\n'
f.write(data)
f.close()
'''

'''
f=open('n1.txt','a+')
data=['python\n','java\n','php\n']
f.writelines(data)
f.close()
'''

# read

'''
f=open('n1.txt')
f=open('n1.txt','rt')
data=f.read(5)
print(data)
# f.close()
data=f.read(20)
print(data)
print("last:",data)
'''

'''
f=open('n1.txt')
f=open('n1.txt','rt')
data=f.readline() # ek line ka data read karega
print(data)
# f.close()
print("last:",data)
'''

'''
f=open('n1.txt')
f=open('n1.txt','rt')
data=f.readlines() # sara datadata read karega
print(data)
# f.close()
print("last:",data)
'''

# Cursor movement

# f=open('n2.txt','x+')
# print(f.tell())


# f=open('n3.txt','a+')
# print(f.tell())


# f=open('n4.txt','w+')
# print(f.tell())

#  tell()

'''
f=open('n1.txt','r+')
print(f.tell()) 
data=f.read(10)
print(data)
print(f.tell())
'''

#   seek()

'''
seek('how many bits are read','from where')
 
                                where= o- starting position
                                       1- current position
                                       2-last position
'''

f=open('n1.txt','rb+')
print(f.tell())
data=f.read(10)
print(data)
print(f.tell())
f.seek(-5,1)
print(f.tell())
f.read(10)
print(f.tell())
f.seek(-15,1)
data=f.read(25)
f.seek(20)
print(f.tell())
f.seek(-1,2)
print(f.tell())
f.seek(-5,2)
data=f.read()
print(data)