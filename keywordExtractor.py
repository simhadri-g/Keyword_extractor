# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:55:26 2018

@author: Simhadri
"""

d = {}

path = input('Enter File path: ')
threshold = int(input("Enter minimum threshold to be a keyword : "))
filteredPassage = []
for line in open(path):
    line = (line.lower())
    #print('start',line,'end of line')
    for i in line:
        if (i<='z' and i >='a') or (i>='A' and i <='Z') :
            filteredPassage.append(i)
            #print(i)
        else:
            filteredPassage.append(" ")
strippedPassage = "".join([str(line) for line in filteredPassage])

#print(strippedPassage)


   
strippedPassage = strippedPassage.split(' ')
setPass =  set(strippedPassage) 
#print(setPass) 

for word in setPass:
    if len(word)<=3 or word == 'with' or word == 'should' or word.startswith('th')== 1:
        pass
    else:
        d[word] = strippedPassage.count(word)
#print(d)       
#print(max(d.values()))
arr = []
for key in d:
    #print(key,'=>',d[key])       
    if d[key]>threshold:
        arr.append(key)

print("\n")
[print("KEYWORDS : ",key,'=>',d[key]) for key in arr]
        
