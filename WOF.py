#create wheel (contains bankrupt, lose a turn, and 17 dollar amounts)
wheel = ['bankrupt', 'loseTurn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 600, 750, 800, 850, 900]
#create word list
word = 'test'
correctLetter = []
#set up accounts for players' money
account1 = []
account2 = []
account3 = []
import random

wordSolved = False

#initialize blank word list with "_"
for char in word:
    correctLetter.append('_')

#Rounds 1 and 2:
#randomly choose word and display with underscores representing each unrevealed letter
#def getWord(word):

#player 1's turn
#ask if they want to solve, spin, or buy a vowel
while not wordSolved:
    userInput = (input('Do you want to spin (type "s"), buy a vowel (type "v"), or solve the puzzle (type "p")?'))
    #if spin, spins wheel
    if userInput == 's':
        wedge = random.choice(wheel)
        print(wedge)
        if wedge == 'bankrupt':
            print('Lose your turn and money')
            #loseTurn and money
        elif wedge == 'lose a turn':
            print('Lose your turn')
            #loseTurn
        else:
            #show letters, multiply wedge by number of instances in word and add to account
            spinInput = (input('Guess a consonant: '))
            if spinInput in word:
                for position in range(len(word)):
                    if word[position] == spinInput:
                        correctLetter[position] = spinInput
            else:
                print('That letter is not in the word.')
            print(correctLetter)
            print(spinInput)
            
       

    #if buy a vowel, check that account has at least $250
    elif userInput == 'v':
        print('vowel')
    
    #if solve, compare to word, if correct, round ends, if incorrect, lose turn and move to next player
    elif userInput == 'p':
        wordGuess = (input('Solve the puzzle:'))
        if word == wordGuess:
            wordSolved = True
            print('Congratulations, you win the round!')
        else:
            #loseTurn
            print('That is not the word. Your turn is over.')

    else:
        print('Choose spin, buy a vowel, or solve the puzzle.')
        