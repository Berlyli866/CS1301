#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""

"""
Function name: stringMultiply()
Parameters: sentence (str), num (int)
Returns: product (int)
"""

def stringMultiply(sentence,num):
    s=str(sentence)
    product=1
    num=int(num)
    if num==0:
        return 0
    elif s.isdigit()==True and num>0:
        L=len(s)
        if num>L:
            for item in res:
                product=product*int(item)
            return product     
    else:
        res = ''.join(filter(lambda i: i.isdigit(), s))
        L=len(res)
        if L ==0:
            return 1
        else:
            if num>=L:
                for item in res:
                    product=product*int(item)
            else:
                for a in range(num):
                    product=product*int(res[a])
            return product


"""
Function name: longestWord()
Parameters: sentence (str)
Returns: a string (str)
"""
def longestWord(sentence):
    big=0
    num=""
    u=str(0)
    count=0
    for i in sentence:
        if i !=" ":
            count +=1
            num +=i
        else:
            if count>big:
                big=count
                u=num
                num=""
                count=0
            elif count==big:
                u=num
                num=""
                count=0
            else:
                num=""
                count=0
    return u 



"""
Function name: drawTriangle()
Parameters: height (int)
Returns: None
"""

def drawTriangle(height):
    print('\n'.join([' '.join([str(i) for _ in range(i)]) for i in range(1,height+1)]))


"""
Function name: populationGrowth()
Parameters: start pop. (int), growth rate (float), expected pop. (int)
Returns: years (int)
"""

def populationGrowth(start_pop,rate,expected_pop):
    start_pop=int(start_pop)
    year=0
    for i in range(1000):
        pop=start_pop*(1+float(rate/100))**i
        year +=1
        if pop <= int(expected_pop):
            continue 
        return year-1   


"""
Function name: marta()
Parameters: path (str), start (str), end (str)
Returns: distance (int)
"""

def marta(path,st,end):
    p=list(path)
    if st==end:
        return 0
    else:
        for item in p:
            if st==item or end==item :
                idx1=p.index(st)
                idx2=p.index(end)
                c=p[idx1:idx2]
                count=0
                for item in c:
                    if item=='-':
                        count=count+1
                return count  



