#Determine which player has the most money

#Get word
word2 = 'stone'

correctLetter = []

#Reveal R-S-T-L-N-E
# 'r','s','t','l','n','e'


for char in word2:
    correctLetter.append('_')

    wordSolved = False

    autoInput = "rstlne"                     
    if autoInput in word2:
            for position in range(len(word2)):
                if word2[position] == autoInput:
                    correctLetter[position] = autoInput

    userInput = (input('Guess a letter: '))                        
    if userInput in word2:
            for position in range(len(word2)):
                if word2[position] == userInput:
                    correctLetter[position] = userInput

    print(correctLetter)

#Ask player for 3 more consonants and one more vowel

#Reveal those letters

#Count down 5 seconds

#If player guesses correctly before time is up, they win
#If not, they lose
