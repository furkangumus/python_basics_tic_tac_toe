# -*- coding: utf-8 -*-
"""
A simple Tic-Tac-Toe Game for console/ terminal/ command prompt

Author : Furkan Gumus
Date   : 03/24/2020
"""
import numpy as np
from random import randint
import os
from platform import system as ps

## Global variables
BOARD = [' ']*9
GAME_STATE = True
MESSAGE = ''
###

def clear_output():
    if ps() == "Windows":
        os.system("cls") # on windows system
    else:
        os.system("clear") # on linux system


def reset_game():
    global BOARD, GAME_STATE
    BOARD = [' ']*9
    GAME_STATE = True


def display_board():
    board = np.array(BOARD).reshape(3,3)
    n = board.shape[0]
    
    for i in range(n):
        print('       |       |      ')
        print('   '+board[i,0]+'   |   '+board[i,1]+'   |   '+board[i,2]+' ')
        print('       |       |      ')
        if i != n-1:
            print("-"*23)


def player_input():
    '''
    Returns: ("player1_marker", "player2_marker")
    '''
    marker = None
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select your marker ['X', 'O'] >> ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    return ('O', 'X')


def status(board, marker):
    '''
    Returns true if there is a winner.
    (status, marker)
    '''
    return (
        (board[0] == board[1] == board[2] == marker) or \
        (board[3] == board[4] == board[5] == marker) or \
        (board[6] == board[7] == board[8] == marker) or \
        (board[0] == board[3] == board[6] == marker) or \
        (board[1] == board[4] == board[7] == marker) or \
        (board[2] == board[5] == board[8] == marker) or \
        (board[0] == board[4] == board[8] == marker) or \
        (board[2] == board[4] == board[6] == marker) 
            )


def select_first():
    return 'X' if not randint(0, 1) else 'O'


def check_position(board, position):
    return board[position] == " "


def check_full_board(board):
    return " " not in board


def pick_update(marker):
    """
    Gets the marker as param and ask user for a position to put the marker
    to that position if it's empty.
    param:
        marker: user marker ['X' or 'O']
    """
    global BOARD
    
    while True:
        try:
            position = int(input(f"Choose where to place your: {marker} [1-9] >> "))-1
            
        except ValueError:
            print("You need to enter an integer in range of [1-9]")
            continue
        else:
            try:
                if check_position(BOARD, position):
                    ## Update position
                    BOARD[position] = marker
                    break
                else:
                    print(f"The {position+1} is already reserved.\n"\
                          +"Try another one...")
                    continue
            except  IndexError:
                print("Please enter an integer in range of [1-9]!")
    

def user_play(marker):
    """
    Gets marker and evaluates the game.
    params:
        marker : string >> "X" or "O"
    """
    global BOARD, GAME_STATE, MESSAGE
    
    ## Updating BOARD
    pick_update(marker)
    
    
    # Check if there is a Winner...
    if status(BOARD, marker):
        clear_output()
        display_board()
        MESSAGE = "VICTORY!!!\n{} wins!".format(marker)
        GAME_STATE = False
    elif check_full_board(BOARD):
        MESSAGE = "It's a TIE!!!"
        GAME_STATE = False    


def replay():
    play_again = input("Do you want to play again? [y|N] >>").upper()
    
    return play_again == "Y"


def game_play(p1, p2, turn):
    reset_game() # reset the globals
    # in order to start a clean game...
    global GAME_STATE, MESSAGE
    

    
    while True:
        # Display BOARD
        clear_output()
        display_board()
        
        if turn == p1: ## Player 1 turn
            user_play(p1)
            
            if not GAME_STATE:
                print("*"*23)
                print(MESSAGE)
                print("*"*23)
                break
            turn = p2
        elif turn == p2: ## Player 2 turn
            user_play(p2)
            
            if not GAME_STATE:
                print("*"*23)
                print(MESSAGE)
                print("*"*23)
                break
            turn = p1



if __name__ == "__main__":
    
    while True:
        
        # Set everything up 
        p1_marker, p2_marker = player_input()
        turn = select_first()
        
        print(f"{'Player 1' if turn == p1_marker else 'Player 2'} will go first")
        
        ready = input("Ready? [y|N] >> ").upper()
        
        if ready == "Y":
            clear_output()
            game_play(p1_marker, p2_marker, turn)
        else:
            break
                    
        if not replay():
            print("I hope you had fun!")
            break