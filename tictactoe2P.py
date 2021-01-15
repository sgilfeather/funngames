#Tic Tac Toe
#MLH Local Hack Day Build - Day 2!

import numpy

player = 1
nexty = ''
count = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
x = [' _  _ ', '( \/ )', ' )  ( ', '(_/\_)']
y = ['  __  ', ' /  \ ', '( () )', ' \__/ ']

print(''' ____  __  ___    ____  __    ___    ____  __  ____  _   
(_  _)(  )/ __)  (_  _)/ _\  / __)  (_  _)/  \(  __)/ \  
  )(   )(( (__     )( / /  \( (__     )( (  O )) _) \_/  
 (__) (__)\___)   (__)\_/\_/ \___)   (__) \__/(____)(_)  \n''')

def switcher(arg, play):
    switchy = {
        'A1' : 1,
        'B1' : 2,
        'C1' : 3,
        'A2' : 4,
        'B2' : 5,
        'C2' : 6,
        'A3' : 7,
        'B3' : 8,
        'C3' : 9
    }
    num = switchy.get(arg, 0)
    #print(str(num) + " num!")
    if num:
        print('run num')
        if board[num-1] == 0:
            board[num-1] = play
            printBoard()
            if play == 1:
                return 2
            else:
                return 1
        else:
            print('This space is taken! Choose another value A1 through C3.')
            return play
    else:
        print('Enter an value A1 through C3 to continue.')
        return play

def parseNum(i,k):
    if board[i] == 1:
        return x[k]
    elif board[i] == 2:
        return y[k]
    else:
        return '      '

def printBoard():
    print('        ( A )    ( B )    ( C )')
    print('       ––––––––––––––––––––––––')
    for i in range(0,3):
        for k in range (0,4):
            if k == 2:
                print('( ' + str(i+1) + ' )  ' + parseNum(3*i,k) + ' | ' + parseNum(3*i+1,k) + ' | '  + parseNum(3*i+2, k))
            else:
                print('       ' + parseNum(3*i,k) + ' | ' + parseNum(3*i+1,k) + ' | '  + parseNum(3*i+2, k))
        print('       ––––––––––––––––––––––––')

def checkWin():
    #check rows
    win = False
    for k in range(0,9,3):
        if board[k] == board[k+1] and board[k+1] == board[k+2]:
            print('Row win for player ' + str(board[k]) + '!')
            win = True
            #return board[k]
    for k in range(0,3):
        if board[k] == board[k+3] and board[k+3] == board[k+6]:
            print('Column win for player ' + str(board[k]) + '!')
            win = True            
            #return board[k]
    if board[0] == board[4] and board[4] == board[8]:
        print('Diagonal win for player ' + str(board[k]) + '!')
        win = True
        #return board[0]
    elif board[2] == board[4] and board[4] == board[6]:
        print('Diagonal win for player ' + str(board[k]) + '!')
        win = True
        #return board[2]
    if not win:
        print("It's a tie!")
    return 0

#runGame     
printBoard()
#implement runGame in a function that also resets the array and
#restarts from keyword input. For now two player, implement computer opp. later 
 
while count < 10:
    if count == 9:
        checkWin()
        print('Do you want to play again? Y / N')
        nexty = input()
        if nexty.strip() == 'Y' or nexty.strip() == 'y':
            count = 0
            board = [0,0,0,0,0,0,0,0,0]
            printBoard()
            print('Enter an value A1 through C3 to continue.')
        elif nexty.strip() == 'N' or nexty.strip() == 'n':
            break
        else:
            pass
    else:
        nexty = input()
        newp = switcher(nexty, player)
        if player != newp:
            player = newp
            count += 1


