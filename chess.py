board_dim = 8
letters = {1: "a", 2: "b",  3: "c", 4: "d", 5: "e", 6: "f",  7: "g", 8: "h"} 
    #letters is a dictionary used when labelling the columns of the board


#white and black are dictionaries containing the chessmen for each player
white = {0: "♔", 1: "♕", 2: "♗", 3: "♖", 4: "♘", 5: "♙"}    
black = {0: "♚", 1: "♛", 2:"♝", 3: "♜", 4: "♞", 5: "♟︎"}


def intro():
    print("Welcome to my chess game!")
    print()
    # ADD BASIC INSTRUCTIONS ON HOW TO PLAY!!!
    
def print_grid(board):
    """ 
    This function should take a board/grid as an input
    and it will return a grid whose columns are labelled with letters
    and numbered rows
    
    """
    
    for i in range(len(board)):
        print(8-i, end = " ")
        
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()
        
    print("  ", end= "")
    for i in range(len(board)):
        print(letters[i + 1], end = " ")
    print()
    
    
def start_board(board):
    """ 
    This function takes a board as an input and will return the
    starting board with all the pieces in the beginning positions
    
    """
    board[1] = [black[5] for i in range(board_dim)]
     
        
    return print_grid(board)

def init_board():
    """" 
    This function takes no inputs and returns an empty 8x8 grid 
    that is the empty chess board (with no pieces yet).
    
    """
    board = [["__" for j in range(board_dim)] for i in range(board_dim)]
    return board


intro()
