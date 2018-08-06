def display_board(board):
    print('\n'*100)
    tictacto = ['     |     |','  ' + board[1] + '  |  '+ board[2] + '  |  ' + board[3],'     |     |','-----------------','     |     |','  ' + board[4] + '  |  '+ board[5] + '  |  ' + board[6], '     |     |', '-----------------', '     |     |','  ' + board[7] + '  |  '+ board[8] + '  |  ' + board[9], '     |     |']
    for i in tictacto:
        print (i)
    print('\n\n')

def player_input():
    player1input = ''
    print('\n'*100)
    while player1input != 'X' or 'O':
        player1input = input('Player 1, would you like to be X or O?  ')
        if player1input.upper() == 'X':
            print('\n'*100)
            input('\n \nPlayer 1 you are X \nPlayer 2 you are O\n\npress Enter to conintue....')
            print('\n'*100)
            break
        elif player1input.upper() == 'O':
            print('\n'*100)
            input('\n \nPlayer 1 you are O \nPlayer 2 you are X\n\npress Enter to conintue....')
            print('\n'*100)
            break
        else:
            print('\n'*100)
            input('\n \nplease enter valid input\n\npress Enter to conintue....  ')
            print('\n'*100)
            continue

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    #straight
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark:
        return True
    #vertical
    elif board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark:
        return True
    #diagonal
    elif board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False

import random

def choose_first():
    global player1
    global player2
    firstplay = random.randint(1,2)
    if firstplay == 1:
        player1 = 'X'
        player2 = 'O'
    elif firstplay == 2:
        player1 = 'O'
        player2 = 'X'

def space_check(board, position):
    if board[position] == " ":
        return True


def full_board_check(board):
    if " " in board:
        return True


def player_choice(board, player):
    while True:
        try:
            whatposition = input('player ' + player + ' what would your next move like to be:  ')
            val = int(whatposition)
            if 1 <= val <= 9 and space_check(board,val):
                return val
                break
            elif val > 9 or val < 1:
                print('sorry!!! try again!!!')
                continue
            else:
                print('that space is filled. Please try again')
                continue
        except (ValueError):
                print("That's not an int!")
                continue


def replay():
    while True:
        playagain = input('Would you like to play again? (yes or no): ')
        if playagain.lower() == 'yes':
            return True
            break
        elif playagain == 'no':
            print('Thanks for playing 🤪')
            break
        else:
            print('Please say yes or no')
            continue






#program start:
print('\n'*100)
input('                     ********************************* \n                     *                               *\n                     *                               *\n                     *    Welcome to Tic Tac Toe!    *\n                     *                               *\n                     *                               *\n                     *********************************\n\n\n\n\n\n\n\n\npress Enter to conintue....')
while True:
    playboard = ["#"," "," "," "," "," "," "," "," "," "]
    exampleboard = ["#","1","2","3","4","5","6","7","8","9"]
    print('\n'*100)
    display_board(exampleboard)
    input('\n\n\nThis is the example board. To enter an X or O on a \nlook at this board to see what number to press.\n\npress Enter to conintue....')
    player_input()
    choose_first()


    while True:

        #Player 1 Turn
        firstmove = player_choice(playboard, player1)
        print(firstmove)
        place_marker(playboard, player1, firstmove)
        display_board(playboard)

        if win_check(playboard, player1):
            print ('You won! Congrats')
            break

        if full_board_check(playboard):
            pass
        else:
            print ('This game was a tie! Good Job!')
            break

        # Player2's turn.
        secondmove = player_choice(playboard, player2)
        place_marker(playboard, player2, secondmove)
        display_board(playboard)

        if win_check(playboard, player1):
            print ('You won! Congrats')
            break

        if full_board_check(playboard):
            pass
        else:
            print ('This game was a tie! Good Job!')
            break


    if replay() != True:
        break
