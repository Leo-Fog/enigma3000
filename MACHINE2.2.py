import random
import pickle

#to type "new line", use "\n"

#Importing key file
file = open('key.txt','rb')
data = pickle.load(file)

#Imporing word_key (for key phrase) file (where each symbol has it's own number)
File = open('DATA/word_key.txt','rb')
wKEY = pickle.load(File)

#Main cycle
while True:
    #Input for text to encode
    ln = input('>')
    run = True
    #Input for key phrase
    Num = (input('Key phrase:'))
    #Converting key phrase to key position numbers
    NUM = []
    for i in range(len(Num)):
        NUM.append(wKEY[Num[i]])
    if len(NUM) < len(ln):
        run = True
    #Repeating key phrase (need to encode all text)
    while run:
        for i in range(len(NUM)):
            NUM.append(NUM[i])
        if len(NUM)>=len(ln):
            run = False
    #Encoding main text
    for i in range(len(ln)):
        print(data[NUM[i]][ln[i]],end='')
    #Making new line
    print('')

