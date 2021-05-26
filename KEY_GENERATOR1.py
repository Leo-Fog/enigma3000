import random
import pickle
import os

#Importing data file (with all symbols, that will be used in key)
file = open('DATA/data.txt','rb')
data = pickle.load(file)

#Result
result = {}

#MAIN
for i in range(100):
    #Importing data file as cache(name is different)
    file = open('DATA/data.txt','rb')
    cash = pickle.load(file)
    #Creating key position
    result[i] = {}
    NUM = len(data)/2
    for y in range(int(NUM)):
        symb1 = random.choice(cash)
        #Removing Symbol 1 from cache
        cash.remove(symb1)
        symb2 = random.choice(cash)
        #Symbol 1 = Symbol 2  and  Symbol 2 = Symbol 1
        result[i][symb1] = symb2
        result[i][symb2] = symb1
        #Removing Symbol 2 from cache
        cash.remove(symb2)

#Entering file name
print('''Please, enter file name.''')
name = input('File name:')
#Saving file
file = open(name+'.txt','wb')
pickle.dump(result,file)
