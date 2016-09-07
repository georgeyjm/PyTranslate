# PyTranslate
# 2.0

from codecs import open
from time import time

# Opens the data file, reads the data file, then splits word by word
print('Importing the dictionary file...')
startTime = time()
file = open('Dictionaries/dictionary.txt', 'r+', 'utf-8')
data = file.readlines()
# Process every words one by one
dictionary = {}
for i in data:
    dictionary[(i.split(':'))[0]] = (i.split(':')[1]) # Adding keys into the dictionary
endTime = time()
print('Finished! Time: %.2f milliseconds'%((endTime-startTime)*1000))
print('Dictionary has in total of %d words.'%len(data))

# Main Program
while True:
    option = input('''\nTranslate [1]\nAdd new word [2]\nSave and exit [3]\nChoose: ''')

    #Translate
    if option == '1':
        sentence = input('\nPlease input an English sentence: ')
        wordOrderTmp = []

        for i in sentence.split():
            i = i.lower()
            try:
                if not dictionary[i]:
                    continue
                if '*' in dictionary[i]:
                    wordOrderTmp = dictionary[i].split('*')
                    print(wordOrderTmp[0], end='')
                    continue
                else:
                    print(dictionary[i], end='')
                if wordOrderTmp:
                    print(wordOrderTmp[1], end='')
                    wordOrderTmp = []
            except Exception:
                print(i, end=' ')
        print()

    #Add new word
    elif option == '2':
        english = input('\nInput the English word: ')
        if english in dictionary:
            print('\nWord exists!')
            print('Current meaning: %s'%dictionary[english.lower()])
            continue
        chinese = input('Input the Chinese translation: ')
        file.write(('\n' + english.lower() + ':' + chinese))
        print('Successfully added \'%s\' into the dictionary'%english)

    #Save and exit
    elif option == '3':
        file.close()
        break

    #Input Fail
    else:
        print('\nInvalid Input!')
