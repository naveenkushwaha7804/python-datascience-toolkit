# Dictionary (immutable) :- 1. Collection of 'key value pair',Where 'key' and 'value' is seperated by (:)
#               2. Represented by { } with comma(,) seperated pairs.  --> {'key':'value','key2':'value2"}
#               3. Key must be unique but value may be dunlicate.
#               4. Mapped data-type.
#               5. Indexing not supported.
#               6. Slicing not supported.
#               7. Mutable in nature.

d={'name':'naveen','age':'21','place':'Bhopal','quali':'B.tech'}
d10={'kaam':'coading'}

#INBUILT FUN (supported)

print(len(d))
print(type(d))
print(id(d))
print(d)
print(max(d))
print(min(d))
#        NOT Supported

print(sum(d))

#            METHODS

# print(d.clear())

d1=d.copy()
print(d,d1)

d2=d.get('name')
#direct v print kr sakte hai
print(d2)   # key se value return karega

print(d.values())

print(d.keys())

print(d.items())   # dictionary to key or values ko touple me convert karega

d3='naveen'
d4=(dict.fromkeys(d3)) # kisi collection ko dictionary me change kar sakte hai keys me convert honge sabhi element 
print(d4)

d.update(d10)
print(d)
print(d10)

# print(d.pop())#  single key se element delete hoga
print(d.pop('name'))
print(d)


# print(d.popitem()) # last item ko remove karega
d.popitem()
print(d) 


# print(d.setdefault())
print(d.setdefault('name','shubham')) # yadi pehe se value define hogi to bahi return karega nahi to key or value add kr dega

                     #OPERATOR HW

# --------------------------------DICTIONARY ME ELEMENT INSERT 

s=['name','email','contact','add']
d=dict.fromkeys(s)
name=input('enter your name :')
email=input('enter your email :')
contact=input('enter your contact :')
add=input('enter your address :')
d['name']=name
d['email']=email
d['contact']=contact
d['add']=add
print(d)
