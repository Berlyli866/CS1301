#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O and CSV
"""

"""
Function name: count_nominations()
Parameters: filename (str), category (str)
Returns: tuple
"""

def count_nominations(fname,cat):
  fin=open(fname,'r')
  text=fin.read()
  fin.close()
  text=text.split('\n\n')
  lis=[]
  for item in text:
    word=item.split('\n')
    lis.append(word)
  movie=""
  for i in lis:
    if i[0]==cat and i[2]=='Winner':
      movie +=i[1]
  print(movie)
  fin = open(fname, 'r')
  text=fin.readlines()
  fin.close()
  count = 0
  for item in text:
    if movie in item:
      count+=1
  if "(" in movie:
    import re
    word = re.findall('\((.*?)\)', movie)
    movie=word[0]
  elif movie=="":
    return ()
  else:
      movie=movie
  return (movie,count)

# cat='Best Sound Editing'
# fname='academyawards.txt'
# count_nominations(fname,cat)
# #
# cat2='Best Visual Effects'
# count_nominations(fname,cat2)
# #
# cat3='Best Adapted Screenplay'
# count_nominations(fname,cat3)
#
# cat4='Best Live Action Short Film'
# count_nominations(fname,cat4)
#
# cat5=''
# count_nominations(fname,cat5)



"""
Function name: categories()
Parameters: filename (str), categoryList (list)
Returns: dictionary
"""
import re
def categories(fname,cat):
  if cat !=[]:
    fin = open(fname, 'r')
    text = fin.read()
    fin.close()
    text = text.split('\n\n')
    lis = []
    for item in text:
      word = item.split('\n')
      lis.append(word)
    dic={}
    for item in cat:
      for i in lis:
        if item==i[0]:
          word =re.split( r'[()]',i[1])
          if item in dic:
             if len(word) >=2:
               dic[item].append((word[0].strip(),word[1].strip()))
             else:
               dic[item].append((word[0].strip(),))
          else:
             if len(word) >=2:
               dic[item]=[(word[0].strip(),word[1].strip())]
             else:
               dic[item]=[(word[0].strip(),)]

    return dic

  else:
    dic={}
  return dic

# cat=['Best Lead Actor','Best Lead Actress','Best Director']
# # cat= ['Best Live Action Short Film','Best Supporting Actress']
# print(categories('academyawards.txt', cat))
#
# cat=["Best Original Screenplay"]
# print(categories('academyawards.txt', cat))
#
# cat=[]
# print(categories('academyawards.txt', cat))

"""
Function name: winner_format()
Parameters: readfile(str), writefile (str), category (str)
Returns: None
"""
def winner_format(fname1,fname2,cat):
  if cat !="":
    fin = open(fname1, 'r')
    text = fin.read()
    fin.close()
    text = text.split('\n\n')
    lis = []
    for item in text:
      word = item.split('\n')
      lis.append(word)
    fname=open(fname2,'w')

    for i in lis:
      if i[0]==cat and i[2]=='Winner':
          fname.write(cat + '\n')
          fname.write('\t1. ')
          fname.write("*Winner* " + i[1]+'\n')
          fname.close()
          break

    fout=open(fname2,'a')
    a=2
    for i in lis:
        if i[0]==cat and i[2]=='Nominated':
            fout.write('\t'+str(a) + '. ')
            fout.write(i[1]+'\n')
            a += 1
    fout.close()
    fout2=open(fname2,'r')
    text=fout2.readlines()
    fout2.close()
    fin2=open(fname2,'w')
    for item in text[:-1]:
      fin2.write(item)
    fin2.write(text[-1].strip('\n'))
    fin2.close()





# fname1 ='academyawards.txt'
# fname2 = 'cat.txt'
# cat = 'Best Supporting Actress'
# cat2='Best Director'
# winner_format(fname1, fname2, cat2)
#
# f=open('cat.txt','r')
# f.readlines()



"""
Function name: data_reformatter()
Parameters: cities (list), years (tuple)
Returns: None
"""
def data_reformatter(city,years):
  try:
    # if years[0]<=2005 and years[1]>=2015:
    #    years=(2005,2015)
    # elif years[0]>2005 and years[1]>=2015:
    #    years=(years[0],2015)
    # elif years[0]<=2005 and years[1]<2015:
    #    years=(2005,years[1])
    fout=open('homeless_2005_2015.csv','r')
    content=fout.readlines()
    fout.close()
    newlis=[]
    for item in content:
        i=item.split(',')
        newlis.append((i[0],i[1],i[2],i[3],i[4]))
    if city !=[""]:
      y = []
      for m in city :
        po=0
        ye=""
        for (id,year,care,state,homeless) in tuple(newlis[1:]):
          if m in id and int(year) in range(years[0],years[1]+1):
            if int(homeless)>=po:
              po=int(homeless)
              ye=year
        y.append((m,ye,po))
    else:
      y=[]
      po=0
      ye=""
      for (id, year, care, state, homeless) in tuple(newlis[1:]):
        if int(year) in range(years[0],years[1]+1):
          if int(homeless) >= po:
            po = int(homeless)
            ye = year
      y.append(('',ye,po))
  # write the result to file
    fin=open('homeless_population.txt', 'w')
    a=1
    for item in y:
      if item[1] !='' or item[2] !=0:
        fin.write(str(a)+'. ')
        fin.write(item[0]+" ")
        fin.write(item[1]+"\n")
        fin.write('Homeless Population: '+str(item[2])+'\n')
        a +=1
    fin.close()
    fout2=open('homeless_population.txt','r')
    text=fout2.readlines()
    fout2.close()
    fin2 = open('homeless_population.txt', 'w')
    for item in text[:-1]:
      fin2.write(item)
    fin2.write(text[-1].strip('\n'))
    fin2.close()
  except:
    return "Invalid Input"




# city= ['Atlanta', 'Tampa', 'Nashville']
# year = (2004, 2009)
# data_reformatter(city, year)
# f=open('homeless_population.txt','r')
# f.readlines()
#
# city = ['Orlando', 'New York', 'Miami']
# year= (2006, 2020)
# print(data_reformatter(city, year))
# year=(2000,2020)
# city=[""]
# data_reformatter(city, year)



"""
Function name: homeless_rate()
Parameters: city1 (str), city2 (str), dates (tuple)
Returns: tuple
"""

def homeless_rate(city1,city2,date):
  try:
    fout = open('homeless_2005_2015.csv', 'r')
    content = fout.readlines()
    fout.close()
    newlis = []
    for item in content:
      i = item.split(',')
      newlis.append((i[0], i[1], i[2], i[3], i[4]))
    y = []
    for m in (city1,city2):
      for (id, year, care, state, homeless) in tuple(newlis):
        if m in id and int(year) in date:
          y.append((m,int(homeless),year))
    print(y)
    if len(y)>2 :
      for i in range(len(y)):
        dif1=y[1][1]-y[0][1]
        dif2=y[3][1]-y[2][1]
        if dif1 > dif2:
             diff=dif2
             C=y[2][0]
        elif dif1< dif2:
             diff=dif1
             C=y[0][0]
        else :
           diff=0
           if y[1][1]<y[3][1]:
             C=y[3][0]
           else:
             C=y[1][0]

        return (C, diff)
    else:
      return 'Invalid Input'
  except:
    return 'Invalid Inpout'


# city1 = 'Tampa'
# city2 = 'Atlanta'
# dates1 = (2005, 2007)
# homeless_change(city1, city2, dates1)
#
#
#
# city3 = 'Orlando'
# city4 = 'Atlanta'
# dates2 = (2005, 2005)
# print(homeless_change(city3, city4, dates2))
# homeless_rate("Miami", "Louisville", (2008, 2009))
# homeless_rate("New Orleans", "Tampa", (2005, 2006))
