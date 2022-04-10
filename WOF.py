#create wheel (contains bankrupt, lose a turn, and 17 dollar amounts)
wheel = ['bankrupt', 'loseTurn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 600, 750, 800, 850, 900]
#create word list
word = 'test'
#set up accounts for players' money
account1 = []
account2 = []
account3 = []

wordSolved = False

#Rounds 1 and 2:
#randomly choose word and display with underscores representing each unrevealed letter
#def getWord(word):

#player 1's turn
#ask if they want to solve, spin, or buy a vowel
while not wordSolved:
    choice = (input('Do you want to spin (type "s"), buy a vowel (type "v"), or solve the puzzle (type "p")?'))
    #if spin, spins wheel
    if choice == 's':
        print('spin')

    #if buy a vowel, check that account has at least $250
    elif choice == 'v':
    #if solve, compare to word
        print('vowel')

    elif choice == 'p':
        print('Solve the puzzle:')
        #if solve, compare to word, if correct, round over, if incorrect, lose turn and move to next player
        if word == wordGuess:
            wordSolved = True
        #else:
            #loseTurn
            #print:('Your turn is over.')


    else:
        print('Choose spin, buy a vowel, or solve the puzzle.')
        