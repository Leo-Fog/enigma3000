import pickle
#Input for all symbols that will be used in key
print('Please, write all symbols you want to use in encryption (without spaces or other separators).')
ln = input('symbols:')
#Creating data list
data = list(ln)
#Entering file name
print('''Please, enter file name.
Note: file will be saved to DATA folder.''')
name = input('File name:')
#Saving file
with open("DATA/"+name+".txt", "wb") as f:
    pickle.dump(data, f)

