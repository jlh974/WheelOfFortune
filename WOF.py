#create wheel (contains bankrupt, lose a turn, and 17 dollar amounts)
wheel = ['bankrupt', 'lose a turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 600, 750, 800, 850, 900]
#create word list
word= []
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
correctLetter = []

import random

#set up accounts for players' money
players = ['player1', 'player2', 'player3']
banks = [0, 0, 0]

f = open(R'Documents\Repos\wheel-of-fortune\word-list.txt')
wordList = f.read().splitlines()
f.close

#Rounds 1 and 2:
#randomly choose word and display with underscores representing each unrevealed letter
#initialize blank word list with "_"

rounds = ['round1','round2']
for i in rounds:
    print(i)

    
    for line in wordList:
        word = random.choice(wordList) 
    print(word)

    
    for char in word:
        
        correctLetter.append('_')
        

    wordSolved = False

    while not wordSolved:
                
        playerBank = zip(players, banks)
        for i, players in enumerate(players):
            print(f'Player {i+1} is up')
            print(banks)
                
                        
            #player 1's turn
            #ask if they want to solve, spin, or buy a vowel        
            userInput = (input('Do you want to spin (type "s"), buy a vowel (type "v"), or solve the puzzle (type "p")?'))
                #if spin, spins wheel
            if userInput == 's':
                    wedge = random.choice(wheel)
                    #bankrupt: loseTurn and money
                    print(wedge)
                    if wedge == 'bankrupt':
                        banks[i] -= banks[i]
                        print('Lose your turn and money')
                        #print(players)
                        
                    #loseTurn: lose turn but keep money
                    elif wedge == 'lose a turn':
                        banks[i] += 0            
                        print('Lose your turn')
                        
                    else:
                        #show letters, multiply wedge by number of instances in word and add to account
                        spinInput = (input('Guess a consonant: '))
                        if spinInput in consonants:
                            if spinInput in word:
                                for position in range(len(word)):
                                    if word[position] == spinInput:
                                        correctLetter[position] = spinInput
                                        banks[i] += wedge
                                        
                            else:
                                print('That letter is not in the word. Next player.')
                                
                        else:
                            print('That is not a consonant.  Lose a turn.')
                            
                        print(correctLetter)
                        print(spinInput)

            #if buy a vowel, check that account has at least $250
            elif userInput == 'v':
                    if banks[i] >= 250:
                        banks[i] -= 250
                        
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
                                
                    else:
                            print('That is not a vowel.  Lose a turn.')
                            
                    print(correctLetter)
                    print(vowelInput)
                
            #if solve, compare to word, if correct, round ends, if incorrect, lose turn and move to next player
            elif userInput == 'p':
                    wordGuess = (input('Solve the puzzle: '))
                    if word == wordGuess:
                        correctLetter.clear()
                        wordSolved = True
                        print('Congratulations, you win the round!')
                        break

                    else:
                        #loseTurn
                        print('That is not the word. Your turn is over.')                        

            else:
                    print('Choose spin, buy a vowel, or solve the puzzle.')

        
