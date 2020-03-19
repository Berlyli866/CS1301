#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries, Try/Except
"""

"""
Function name: average_scores()
Parameters: exam_info (dict)
Returns: list
"""

from statistics import mean
def average_scores(dic):
    lis=[]
    for item in dic.keys():
        if len(dic[item])==0:
            lis.append((item,None))
        else:
            avg=round(mean(dic[item]),2)
            lis.append((item,avg))
    return lis

"""
Function name: class_finder
Parameters: courseDict (dict), friendsList (list)
Returns: list
"""

from collections import defaultdict

def class_finder(course,friend):
    goodclass=[]
    count=defaultdict(list)
    for item in course.keys():
        for name in friend:
            if name in course[item]:
                count.setdefault(item, []).append(name)
    d = dict((item, tuple(name)) for item, name in count.items())
    for item in d.keys():
        if len(d[item])>=2:
            goodclass.append(item)
    return goodclass

"""
Function name: security_clearence()
Parameters: info (list of tuples)
Returns: dict
"""
def check_dict(dictionary, key, val):
    if key not in dictionary.keys():
        dictionary[key] = val
    else:
        if isinstance(dictionary[key], list):
            dictionary[key].append(val[0])
        if isinstance(dictionary[key], dict):
            check_dict(dictionary[key], list(val.keys())[0], list(val.values())[0])
            

def security_clearance(some_list):
    dictionary = {}
    for tuple_item in some_list:
        check_dict(dictionary, tuple_item[0], {tuple_item[1] : [tuple_item[2]]})
    return dictionary


#type 2 
def security_clearence2(lis):
    lis=tuple(lis)
    dic={}
    for k,s,n in lis:
        if k in dic.keys():
            if s in dic[k]:
                dic[k][s] +=[n]
            else:
                dic[k].update({s:[n]})    
        else:
            dic[k]={s:[n]}
    return dic 

"""
Function name: find_me()
Parameters: people (dict), person1 (str), person2 (str)
Returns: int
"""


def find_me(p,p1,p2):
    if p1!=p2 and p1 in p.keys() :
        a=0
        while p[p1]!=p2:
            if p[p1] not in p:
                a=None
                break
            else:    
                p1=p[p1]
                print(p1)
                a +=1
                
    elif p1 not in p.keys():
        a=None                    
    else:
        a=0
    return a




"""
Function name: error_finder()
Parameters: numList (list), indexList (list)
Returns: tuple
"""

from statistics import mean
def error_finder(num,ind):
    value=[]
    error= {"IndexError": 0, "TypeError": 0}
    for item in ind:
        if type(item)==int:
            if item<=len(num)-1:
                value.append(num[item])
            else:
                a="IndexError"
                error[a] +=1
        else:
            a='TypeError'
            error[a] +=1
    if value !=[]:
        avg=float(mean(value))
    else:
        avg=0
    return (avg,error)

