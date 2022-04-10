#create wheel (contains bankrupt, lose a turn, and 17 dollar amounts)
wheel = ['bankrupt', 'lose a turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 600, 750, 800, 850, 900]
#create word list
word = 'test'
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
correctLetter = []
#set up accounts for players' money
account1 = 0
account2 = []
account3 = []

import random



players = list(('player1','player2','player3'))



#Rounds 1 and 2:
#randomly choose word and display with underscores representing each unrevealed letter
#initialize blank word list with "_"

rounds = list(('round1','round2'))
for i in rounds:

    wordSolved = False

    for char in word:
        correctLetter.append('_')


    #player 1's turn
    #ask if they want to solve, spin, or buy a vowel
    while not wordSolved:
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
            #loseTurn: lose turn but keep money
            elif wedge == 'lose a turn':
                account1 += 0            
                print('Lose your turn')
                print(account1)
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
                        print('That letter is not in the word.')
                else:
                    print('That is not a consonant.  Lose a turn.')
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
            else:
                    print('That is not a vowel.  Lose a turn.')
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

        else:
            print('Choose spin, buy a vowel, or solve the puzzle.')
            