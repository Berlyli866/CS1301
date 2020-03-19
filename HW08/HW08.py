#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW08 - APIs
"""


"""
Function Name: cookFast()
Parameters: dish name (str), amount of minutes (int)
Returns: list of foods (list)
"""
import requests
def cookFast(dish,time):
  base_url = "https://api.spoonacular.com/recipes/search"
  key = "/?apiKey=ac1dab45d05a4efb9c8b859aba21ea91"
  para="&query="+dish
  url = base_url +key+para
  r= requests.get(url)
  data=r.json()
  lis=[]
  for item in data['results']:
    if item['readyInMinutes']< time and item['servings']>=4:
      lis.append(item['title'])
  return lis

# print (cookFast("pasta", 30))
# print (cookFast("sandwich", 35))
# print (cookFast("burger", 50))
# print(cookFast("soup", 30))


"""
Function Name: nutrients()
Parameters: nutrient name (str), minimum amount (int), maximum amount (int)
Returns: list of foods (list)
"""


def nutrients(name,mi,ma):
  base_url='https://api.spoonacular.com/recipes/findByNutrients'
  key="/?apiKey=ac1dab45d05a4efb9c8b859aba21ea91"
  name=name.replace(' ','')
  para='&min'+name+"="+str(mi)+'&max'+name+"="+str(ma)
  url = base_url + key+para
  r=requests.get(url)
  data=r.json()
  c=[]
  for item in data:
    c.append(item['title'])
  return c




# print(nutrients("VitaminB12", 200, 240))
# print(nutrients("Zinc", 2, 10))
# print(nutrients("Calcium", 1500, 1510))
# print(nutrients("Saturated Fat", 100, 160))


"""
Function Name: groceryTime()
Parameters: recipeID (int), list of allergies (list of str)
Returns: dictionary (dict)
"""
import requests
def groceryTime(id,alis):
  base_url='https://api.spoonacular.com/recipes/{}/information'.format(str(id))
  key = "/?apiKey=ac1dab45d05a4efb9c8b859aba21ea91"
  url = base_url + key
  para={'includeNutrition':'False'}
  r=requests.get(url,params=para)
  d=r.json()
  name=[]
  for i in d['extendedIngredients']:
    if i['name'] not in alis:
      name.append(((i['aisle'],i['name'],i["measures"]['us']["amount"])))
  if name !=[]:
    D = {}
    for key,na,amount in name:
      if key in D.keys():
        D[key] +=[(na,amount)]
      else:
        D[key]=[(na,amount)]
  else:
    D={}
  return D

# id=1003464
# als=["blueberries", "flour", "nutmeg", "rhubarb"]
# print(groceryTime(id, als))

#
# recipeID = 716429
# allergies = ["butter", "cloves", "white wine", "cheese"]
# print (groceryTime(recipeID, allergies))



"""
Function name: animalPopulation()
Parameters: maximum (int)
Returns: list of tuples
"""

def animalPopulation(maxmum):
  baseurl='http://www.bloowatch.org'
  species='/developers/json/species'
  url=baseurl+species
  r=requests.get(url)
  data=r.json()
  lis=[]
  for item in data['allSpecies']:
    lis.append((item['name'], item['population'].split('-')))
  finalis=[]
  for name,num in lis:
    a=num[0].replace(',','')
    if a !='unknown':
      if int(a) < maxmum:
        finalis.append((name,int(a)))
  return finalis


# print(animalPopulation(10000))
#
# print (animalPopulation(3500))




"""
Function_Name: encyclopedia()
Parameters: endangerment level (str)
Returns: dictionary of animals (dict)
"""

def encyclopedia(e_level):
  if e_level in ('Vulnerable','Endangered','Critically Endangered') :
    baseurl = 'http://www.bloowatch.org'
    species = '/developers/json/species'
    url = baseurl + species
    r = requests.get(url)
    data = r.json()
    dic={}
    for item in data['allSpecies']:
      if item['status']==e_level:
          dic[item['name']]=item['description'].split('.')[0]+'.'
        # else:
        #   dic[item['name']].replace(item['description'])
    return dic
  else:
    return None

# print (encyclopedia("Vulnerable"))
# # a=encyclopedia("Vulnerable")
# # print(a.keys())
# #
# # print (encyclopedia("Critically Endangered"))
# print (encyclopedia("Endangered"))
# a=encyclopedia("Endangered")
# a.keys()
