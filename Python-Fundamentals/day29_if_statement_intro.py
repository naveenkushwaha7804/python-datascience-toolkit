 # CONDITIONAL STATEMENT

# 1 - if statement  (for single condition)                                 if - independent 
# 2 - if-else statement                                                    else or elif - dependent
# 3 - if -elif statement (for multiple condition)
# 4 - if-elif-else statement

# -------------------------------------------

# x=int(input('enter a no'))

# if x>=1:
#    print(f'given no. {x} positive')
# else:
#    print(f'given no. {x} negative or zero')

# ----------------------------------

# y=int(input('enter a no'))

# if y>=1:
#    print(f'no. {y} is positive')
# elif y<=1:
#    print(f'no.{y} is negative')

# -----------------------------------------

# z=int(input('enter a no'))
# if z<0:
#    print(f'no. {z} is negative') 
# elif z==0:
#    print(f'no. {z} is zero')
# else:
#    print(f'no. {z} is positive')
   
# age=float(input('enter your age :'))

# if 0<age<=18:
#    print('your are child')
# elif 19<=age<=60:
#    print('your are adult')
# elif 61<age<=100:
#    print('your are older')
# else: 
#    print('invalid output')

'''
hindi=float(input('enter your hindi marks :'))
english=float(input('enter your english marks :'))
pyhsics=float(input('enter your physics marks :'))
chemistry=float(input('enter your chemistry marks :'))
bio=float(input('enter your bio marks :'))
if 0<=hindi<=100:
    if 0<=english<=100:
       if 0<=physics<=100:
          if 0<=chemistry<=100:
             if 0<=bio<=100:
                 average=(hindi+english+bio+chemistry+pyhsics)/5
                 if 1<average<=34:
                    print('D grade')
                 elif 34<average<=44:
                     print('C grade')
                 elif 45<average<=60:
                     print('B grade')
                 elif 61<average<=75:
                     print('B+ grade')
                 elif 70<=average<=85:
                     print('A grade')
                 elif 85<average<=100:
                     print('A+ grade')
                 print(f'your marks percentage is {average} :')
             else :
                print(f'given  marks is invalid')
          else :
              print(f'given  marks is invalid')
       else :
          print(f'given  marks is invalid')
    else :
       print(f'given  marks is invalid')
else :
   print(f'given  marks is invalid')'''

hight=int(input("enter hight"))
base=int(input("enter base"))
print((1/2)*hight*base)
