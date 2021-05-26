import pickle
import random

#Importing data file (with all symbols, that will be used in key)
file = open('DATA/data.txt','rb')
data = pickle.load(file)
#Number of key positions
number = 100
#Result
result = {}
#Numbers list (need to make number for each symbol)
nums = []

#Crating main numbers
for i in range(number):
    nums.append(i)
#Adding extra number to "nums" 
for i in range(len(data)-number):
    nums.append(random.randint(0,number-1))
#Main algorithm
for i in range(len(data)-1):
    #Random letter
    let = random.choice(data)
    #Random number
    num = random.choice(nums)
    #Making letter assosiated to number
    result[let] = num
    #Removing letter and number from lists (to avoid repeating)
    data.remove(let)
    nums.remove(num)
file.close()
#Entering file name
print('''Please, enter file name.
Note: file will be saved to DATA folder.''')
name = input('File name:')
#Saving file
with open("DATA/"+name+".txt", "wb") as f:
    pickle.dump(result, f)

