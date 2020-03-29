#!/usr/bin/env python
# coding: utf-8

# In[40]:


from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[41]:


def player_input():
    
    marker = raw_input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[42]:


def place_marker(board, marker, position):
    board[position] = marker


# In[43]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


# In[44]:


def space_check(board, position):
    
    return board[position] == ' '


# In[45]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[47]:


def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        print('Choose your next position: (1-9) ')
        print("7   8   9")
        print("4   5   6")
        print("1   2   3")
        position = raw_input()
    return int(position)


# In[48]:


def replay():
    
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:


print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    game_on = True

    while game_on:
        display_board(theBoard)
        position = player_choice(theBoard)
        place_marker(theBoard, player1_marker, position)

        if win_check(theBoard, player1_marker):
            display_board(theBoard)
            print('Player 1 has won!')
            game_on = False
            break
        else:
            if full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
                
        display_board(theBoard)
        position = player_choice(theBoard)
        place_marker(theBoard, player2_marker, position)

        if win_check(theBoard, player2_marker):
            display_board(theBoard)
            print('Player 2 has won!')
            game_on = False
            break
        else:
            if full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break

    if not replay():
        break


# In[ ]:




