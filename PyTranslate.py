# PyTranslate 1.0

import codecs
import time
from math import *

#Setting the Master Password
masterPwd = int(pow(int(fabs(factorial(acos(1))-sqrt(4)+14641**(1/4)-tan(radians(45))*tan(pi/4)-acos(-0.5)*180/pi)+fmod(198279793,22031087)),(1/sqrt(sqrt(sqrt(sqrt(sqrt(4294967296))))))))
j
# Opens the data file, reads the data file, then splits word by word
print('Importing the dictionary file...')
startTime = time.clock()
file = codecs.open('Dictionaries/dictionary2.txt', 'r+', 'utf-8')
data = (file.read()).split('\n')
# Process every words one by one
dictionary = {}
for i in data:
    dictionary[(i.split(':'))[0]] = (i.split(':')[1]) # Adding keys into the dictionary
endTime = time.clock()
print('Finished! Time: %s milliseconds'%(str((endTime-startTime)*1000))[:4])
print('Dictionary has in total of %d words.'%len(data))

# Main Program
while True:
    option = input('''\nTranslate [1]\nAdd new word [2]\nSave and exit [3]\nChoose: ''')

    #Translate
    if option == '1':
        sentence = input('\nPlease input an English sentence: ')
        splited = sentence.split()

        for i in splited:
            if i.lower() in dictionary:
                print(dictionary[i.lower()],end='')
            else:
                print(i,end=' ')
        print()

    #Add new word
    elif option == '2':
        inputPwd = input('\nInput the Master Password in order to access this: ')
        if int(inputPwd) == masterPwd:
            print('Password Correct!')
            english = input('\nInput the English word: ')
            if english in dictionary:
                print('\nWord exists!')
                print('Current meaning: %s'%dictionary[english.lower()])
                continue
            chinese = input('Input the Chinese translation: ')
            file.write(('\n' + english.lower() + ':' + chinese))
            print('Successfully added \'%s\' into the dictionary'%english)
        else:
            print('Incorrect Password!')

    #Save and exit
    elif option == '3':
        file.close()
        break

    #Input Fail
    else:
        print('\nBe Sensible!')
