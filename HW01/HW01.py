#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements
Name:Beili Li
GTID:903461609
"""

"""
Function name: calorie_count()
Parameters: no parameters
Return value: None
"""

def calorie_count():
    a=input("How many hamburgers would you like? ")
    b=input("How many orders of french fries would you like? ")
    c=input("How many carrot sticks would you like? ")
    d=input("How many minutes did you walk? ")
    result=int(a)*400+int(b)*200+int(c)*25-int(d)*5
    print(a,'hamburgers,', b, 'orders of french fries,',c, 'carrot sticks,',
          'and',d, 'minutes walked is' ,result, 'calories.')
              
"""
Function name: cone_volume()
Parameters: no parameters
Return value: None
"""
import math
pi = math.pi
def cone_volume():
    a=input("What is the height of the cone? ")
    b=input("What is the radius of the cone? ")
    pi = math.pi
    v=pi*float(b)**2*(float(a)/3)
    v=round(v,2)
    print('The volume of a cone with a height of', float(a),'and a radius of',
          float(b), "is {}.".format(v))
    
    

"""
Function name: watch_time()
Parameters: no parameters
Returns: None
"""

def watch_time():
    m=input("How many movies have you watched? ")
    b=input("How many TV show episodes have you watched? ")
    t=int(m)*110+int(b)*25
    t1=t//60
    t2=t%60
    print('By watching', int(m), 'movies and', int(b),'TV show episodes, you have spent', int(t1), 
          'hour(s) and', int(t2), 'minutes on Disney+.')
    
"""
Function name: liquid_conversion()
Parameters: no parameters
Returns: None
"""

def liquid_conversion():
    c=input("How many cups of water did you drink? ")
    c=int(c)
    gallon=c//16
    a=c%16
    quart=a//4
    b=a%4
    pint=b//2
    cup=c-gallon*16-quart*4-pint*2
    print('You drank', gallon ,'gallon(s),', quart ,
          'quart(s),',pint,'pint(s), and', cup, 'cup(s) of water.')

"""
Function name: savings_calculator()
Parameters: no parameters
Returns: None
"""

def savings_calculator():
    p=input("What is the principal? ")
    r=input("What is the interest rate? ")
    t=input("How many months have passed? ")
    money=float(p)*(1+float(r)/100*(int(t)/12))
    money=round(money,2)
    print("You will have ${}".format(money),'at the end of', t, 'months.')
    

