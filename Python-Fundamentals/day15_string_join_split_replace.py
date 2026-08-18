#    JOIN

# syntex=  seprator.join([elements])
s1='python'
s2='java'
s3='php'
#l=[s1,s2,s3]
# s=' '.join([s1,s2,s3])
# print(s)

# ---------------------------------
s2='python'
s3='10'
print(' '.join([s2,s3]))
# print(' '.join(['python','10'])) / error
# ---------------------------------
   
    #  SPLIT

    # syntex= string.split('seprator')
s4='This is python'
# string.split('seprator,'how many times')
l=s4.split()
l=s4.split('s',1)
l=s4.split('s',2)  #perameter for kaha se split karna hai or kitni baar karna hai
print(l)

# --------------------------------

    # REPLACE

S5='this is python'
print(S5.replace('i','Z',1)) # kisko kisse replace karna hia
# isko - kisse - kitni baar replace karna hai
print(S5.replace('this','Z',1))

 #   OPERATOR

s7,s8='python','Java'
print(s7+s8)
#  +=concation
# print(s7-s8)
print(s7*5)
# print(s7/5)
# print(s7%5)
# print(s7//5)
# print(s7**5)
# ONLY TWO OPERATORS ARE USABLE IN STRING
print('a'>'A') # TRUE (work with asqui value)
print('Python'>'java')
print('Python'>'pava')
print('Python'<'pava')
# follow dictionary
print('pava'=='pava')

      #logical operator [AND]

# if any string empty  than print False
# if true than print last string
# jis String ki bajah se false hoga usi ko print karega
s9='python'
s10='java'
#
j='a'
print(bool('j'))
i=''
k='naveen'
#print(i and k) # empty output print hoga
  
    #logical operator [OR]
 
#   jo pehla true hoga bahi o/p hoga
# yadi dono empty honge to false hoga than last false print hoga
l='python java'
m='java'
n=''
# print(l or m)
# print(m or l)
# print(m or n)
# print(n or m)

   #logical operator [not] nahi hota




