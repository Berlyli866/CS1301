#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW05 - Advanced Lists, Tuples, and Modules
"""

"""
Function name: summer_job()
Parameters: jobs (list of tuples)
Returns: string
"""

def summer_job(jobs):
    sa=-1
    for position,pay,hours in jobs:
        salary=float(pay)*int(hours)
        if salary >sa:
            sa=salary
            job=position        
    return job


"""
Function name: wasted_food()
Parameters: meals (list of list and tuples)
Returns: tuple
"""

def wasted_food(food):
    p=100
    wast=1000
    for name in food[0]:
        for i in range(len(food[1:])):
            por=round(food[1:][i][1]/food[1:][i][0]*100,2)
            if por<p:
                p=por
                na=food[0][i]
            elif por==p:
                if food[1:][i][1]<wast:
                    wast=food[1:][i][1]
                    na=food[0][i]
               
    return (na,p)  


"""
Function name: ancestors()
Parameters: names (list), surname (str)
Returns: list
"""

def ancestors(namelist,surname):
    result=[]
    for item in namelist:
        if len(item.split(" "))==2:
            a=item.split(" ")
            su=a[1]
            if su==surname:
                b=a[0]
                if b not in result:
                    result.append(b)
    return result   
                


"""
Function name: trigonometry
Parameters: degree (str), operation (str)
Returns: float
"""

def trigonometry(a,operator):
    import math
    if operator =='cosine':
        value=round(math.cos(float(a[:-1])/180*math.pi),2)       
    elif operator=='sine':
        value=round(math.sin(float(a[:-1])/180*math.pi),2) 
    elif operator=='tangent': 
        value=round(math.tan(float(a[:-1])/180*math.pi),2)
    else:
        value=round(float(a[:-1])/180*math.pi,2)
    return value  


"""
Function name: days_of_the_week()
Parameters: birthdays (list of tuples), year (int)
Returns: list
"""

def days_of_the_week(birth_list,year):
    import calendar
    n=[]
    for days,month,name in birth_list:
        day=calendar.weekday(year, month, days)
        if day==4 or day==5:
            n.append(name)
    return n

"""
Function name: donation_amount()
Parameters: donations (list of strs)
Returns: float
"""

def conversion(aStr):
    aStr = aStr[1:]
    final = float(aStr)
    return final


def donation_amount(dlist):
    total=0
    for item in dlist:
        new_item=conversion(item)
        total +=new_item
    return total  
