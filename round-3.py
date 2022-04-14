#Determine which player has the most money

#Get word
word=[]
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
correctLetter = []

import random

f = open(R'Documents\Repos\wheel-of-fortune\word-list.txt')
wordList = f.read().splitlines()
f.close

for line in wordList:
    word = random.choice(wordList)
print(word)

for char in word:
    correctLetter.append('_')


wordSolved = False

while not wordSolved:        


#Reveal R-S-T-L-N-E
# 'r','s','t','l','n','e'

        givenLetters = 'r,s,t,l,n,e'
        slicedLetters = givenLetters.split(',')
        for i, autoInput in enumerate(slicedLetters):
            if autoInput in word:
                for position in range(len(word)):
                    if word[position] == autoInput:
                        correctLetter[position] = autoInput
            print(correctLetter)

        


        #Ask player for 3 more consonants and one more vowel
        conInput = (input('Guess 3 more consonants: '))
        if conInput in consonants:
                if conInput in word:
                    for position in range(len(word)):
                        if word[position] == conInput:
                            correctLetter[position] = conInput

                else:
                    print('That letter is not in the word.')
        else:
            print('That is not a consonant.')



        #Reveal those letters

        #Count down 5 seconds

        #If player guesses correctly before time is up, they win
        #If not, they lose
