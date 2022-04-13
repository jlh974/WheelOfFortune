#create wheel (contains bankrupt, lose a turn, and 17 dollar amounts)
wheel = ['bankrupt', 'lose a turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 600, 750, 800, 850, 900]
#create word list
word=[]
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
correctLetter = []
#set up accounts for players' money
account1 = 0
account2 = 0
account3 = 0

#Rounds 1 and 2:
#randomly choose word and display with underscores representing each unrevealed letter
#initialize blank word list with "_"

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

rounds = ['round1','round2']
for i in rounds:
    print(i)

    #players = ['Joe','Mary','Jill']

    #for i, player in enumerate(players):
        #print(f'Player {i}: {player}')        
        
    while not wordSolved:        

    #player 1's turn
    #ask if they want to solve, spin, or buy a vowel
            
        userInput = (input('Do you want to spin (type "s"), buy a vowel (type "v"), or solve the puzzle (type "p")?'))
        #if spin, spins wheel
        if userInput == 's':
            wedge = random.choice(wheel)
            #bankrupt: loseTurn and money
            print(wedge)
            if wedge == 'bankrupt':
                account1 -= account1
                print('Lose your turn and money')
                print(account1)
                continue
            #loseTurn: lose turn but keep money
            elif wedge == 'lose a turn':
                account1 += 0            
                print('Lose your turn')
                print(account1)
                #continue
            else:
                #show letters, multiply wedge by number of instances in word and add to account
                spinInput = (input('Guess a consonant: '))
                if spinInput in consonants:
                    if spinInput in word:
                        for position in range(len(word)):
                            if word[position] == spinInput:
                                correctLetter[position] = spinInput
                                account1 += wedge
                                print('You have $',account1)
                    else:
                        print('That letter is not in the word. Next player.')
                        continue
                else:
                    print('That is not a consonant.  Lose a turn.')
                    #continue
                print(correctLetter)
                print(spinInput)

        #if buy a vowel, check that account has at least $250
        elif userInput == 'v':
            if account1 >= 250:
                account1 -= 250
                print('You have $',account1)
            else:
                print('You don\'t have enough money to buy a vowel.  Spin or solve.')
            vowelInput = (input('Guess a vowel: '))
            if vowelInput in vowels:
                    if vowelInput in word:
                        for position in range(len(word)):
                            if word[position] == vowelInput:
                                correctLetter[position] = vowelInput
                    
                    else:
                        print('That letter is not in the word.')
                        #continue
            else:
                    print('That is not a vowel.  Lose a turn.')
                    #continue
            print(correctLetter)
            print(vowelInput)
        
        #if solve, compare to word, if correct, round ends, if incorrect, lose turn and move to next player
        elif userInput == 'p':
            wordGuess = (input('Solve the puzzle: '))
            if word == wordGuess:
                wordSolved = True
                print('Congratulations, you win the round!')
            else:
                #loseTurn
                print('That is not the word. Your turn is over.')
                #continue

        else:
            print('Choose spin, buy a vowel, or solve the puzzle.')           