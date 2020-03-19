#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW02 - Returns and Conditionals 
"""

"""
Function name: co2emissions()
Parameters: trolleys (int), buses (int), cars (int)
Return value: Str
"""

def co2emissions(trolleys,buses,cars):
    amount=int(trolleys)*233+int(buses)*299+int(cars)*371
    if amount <= 250:
        return "Great"
    elif amount >250 and amount < 1000 :
        return "Not Good"
    else:
        return "Bad!!"

"""
Function name: supportRally()
Parameters: students supporting movement (float), percent of students at rally (float), support level (str)
Return value: str or float
"""

def supportRally(support,rally,level):
    if level=='Outstanding support':
        p=0.9
    elif level=='Significant support':
        p=0.8
    elif level=='Moderate support':
        p=0.7
    a=float(p)-((1-float(rally))*float(support))
    b=round(float(a)/float(rally)*100,2)      
    if b >100:
        return 'Not Possible'
    else:
        return b

"""
Function name: isRallySuccessful()
Parameters: level of evidence (int), students supporting movement (float), percent of students at rally (float), support level (str)
Return value: boolean
"""

def isRallySuccessful(evidence,support,rally,level):
    b=supportRally(support,rally,level)
    if b=='Not Possible' or evidence <= 6:
        return False
    elif b <=100 and evidence >6:
        return True 
        

"""
Function name: spreadingFire()
Parameters: square miles on fire (int), endangerment limit (int)
Return value: str
"""
def spreadingFire(fire_mile,limit):
    a=int(fire_mile)-int(limit)
    b=a//100
    if b<1:
        return 'Danger Level: 0; Proceed with caution'
    if b>=1 and b<= 4:
        level=b
        return 'Danger Level: {}; Firebreak and Airdrop'.format(level)
    elif b>4:
        level=b
        return 'Danger Level: {}; Evacuate and Full Protocol'.format(level)

 

"""
Function name: recycle()
Parameters: soda (int), bags (int), forks (int), caps (int)
Return value: None
"""

def recycle(bottles,bags,forks,caps):
    pete_w=37.3*int(bottles) 
    hdpe_W=5*int(bags)
    pp_w=2.5*int(forks)+2.4*int(caps)
    pete=int(bottles)
    hdpe=int(bags)
    pp=int(forks)+int(caps)
    gi=0
    yi=0
    ri=0
    if pete<5 and pete_w>60:
        gi +=pete
        if pp>10 and pp_w >60:
            gi =+pp 
        elif pp_w<60 or hdpe !=0:
            yi=pp+hdpe
        elif pp<10 and pp_w>60:
            ri +=pp
    elif pete>5 and pete_w>60:
        yi +=pete
        if pp_w<60 or hdpe!=0:
            yi=yi+pp+hdpe  
        elif pp<10 and pp_w>60:
            ri +=pp              
    elif pete_w<60:
        ri +=pete
        if pp<10 and pp_w>60:
            ri +=pp
        elif pp_w<60 or hdpe!=0:
            yi=yi+pp+hdpe 
    return 'Green:{}, Yellow:{}, Red:{}'.format(gi,yi,ri)



