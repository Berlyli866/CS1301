#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing, and Lists
"""

"""
Function name: noteTaker()
Parameters: class (str), courses (list)
Returns: boolean
"""

def noteTaker(notes):
    symbol='.,?!@:'
    new= ""
    l=[]
    j=[i for i,j in enumerate(notes) if j.isupper()]
    if j[0]!=0:
            notes=notes[j[0]:]
            for i in range(len(notes)):
                if i <=int(len(notes)-3):
                    if notes[i] in symbol and  notes[i+2].isupper():
                        new +=notes[i]
                    elif notes[i] not in symbol:
                        new +=notes[i]
                elif i <len(notes)-1:
                    if notes[i] not in symbol:
                      new +=notes[i]
            else:
                new +=notes[i]          
            
        
    else:
        for i in range(len(notes)):
            if i <=int(len(notes)-3):
                if notes[i] in symbol and  notes[i+2].isupper():
                    new +=notes[i]
                elif notes[i] not in symbol  :
                    new +=notes[i]
            elif i !=len(notes)-1:
                 if notes[i] not in symbol:
                    new +=notes[i]
            else:
                new +=notes[i] 
        
    return new


"""
Function name: foodDesertLocator()
Parameters: cities (list)
Returns: (list)
"""


def foodDesertLocator(cities):
    a=[]
    for i in range(len(cities)):
        if i%2==1:
            a.append(cities[i])
    avg=sum(a)/len(a)
    c=[]
    for item in a:
        if item >avg:
            c.append(item)
    b=[i-1 for i,j in enumerate(cities) if j in c] 
    city=[]
    for item in b:
        city.append(cities[item])
    return city   
    

"""
Function name: messageEncoder()
Parameters: message (string)
Returns: encodedMessage (string)
"""

def messageEncoder(message):
    if message !="":
        c=[]
        message=message.split()
        for i in range(len(message)):
            if i %2 ==0:
                upper=message[i].upper()
                c.append(upper)
            else:
                lower=message[i].lower()
                c.append(lower)
        c=" ".join(c)
    else:
        c=None
        
    return c


"""
Function name: courseCreator()
Parameters: courseList (list)
Returns: newCourse (str)
"""


def courseCreator(courselist):
    if courselist !=[]:
        Num=[]
        Char=[]
        for i in range(len(courselist)):
            a=courselist[i]
            b=list(a)
            number=""
            char=""
            for item in b:
                if item.isdigit():
                    num=item
                    number +=num
                else:
                    char +=item 
            Num.append(number)
            Char.append(char)
        Num=[int(item) for item in Num]     
        new_num=sum(Num)//len(Num)
        new_num=str(new_num)
    
        if len(new_num)==1:
            new_num=str("000")+str(new_num)
        elif len(new_num)==2:
            new_num=str("00")+str(new_num)
        elif  new_num==3:
            new_num=str("0")+str(new_num)
        else:
            new_num=new_num         
        new_course=str(Char[1])+str(new_num)

    else:
        new_course=None
    return new_course


"""
Function name: compoundWords()
Parameters: wordsList (list), num (int)
Returns: matchedWords (list)
"""

def compoundWords(wordsList,num):
    if wordsList !=[]:
        l=[j for i,j in enumerate(wordsList) if num ==len(j)]
        if l ==[]:
            count=0
            W=[]
            for i in range(len(wordsList)):
                a=wordsList[i]
                count +=1  
                for j in range(count,len(wordsList)):
                    b=wordsList[j]
                    L=len(a)+len(b)
                    if L==num:
                        new=str(a)+str(b)
                        W.append(new)
        else:
            W=l
    else:
        W=None
    return W   
