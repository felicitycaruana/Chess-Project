board_dim = 8
letters = {1: "a", 2: "b",  3: "c", 4: "d", 5: "e", 6: "f",  7: "g", 8: "h"} 
    #letters is a dictionary used when labelling the columns of the board


#white and black are dictionaries containing the chessmen for each player
white = {0: "♔", 1: "♕", 2: "♗", 3: "♖", 4: "♘", 5: "♙"}    
black = {0: "♚", 1: "♛", 2:"♝", 3: "♜", 4: "♞", 5: "♟︎"}

# this line is for usability in dark mode so the pieces are the correct colour
white, black = black, white

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
        print(8-i, end = "\t")
        
        for j in range(len(board[i])):
            print(board[i][j], end = "\t")
        print()
        
    print(" ", end= "\t")
    for i in range(len(board)):
        print(letters[i + 1], end = "\t")
    print()
    
    
def start_board(board):
    """ 
    This function takes a board as an input and will return the
    starting board with all the pieces in the beginning positions
    
    """
    #add the pawns to their starting position
    board[1] = [black[5] for i in range(board_dim)]
    board[6] = [white[5] for i in range(board_dim)]
    
    #add the rooks
    board[0][0] = black[3]
    board[0][7] = black[3]
    board[7][0] = white[3]
    board[7][7] = white[3]
    
    #add the knights
    board[0][1] = black[4]
    board[0][6] = black[4]
    board[7][1] = white[4]
    board[7][6] = white[4]
        
    #add the bishops
    board[0][2] = black[2]
    board[0][5] = black[2]
    board[7][2] = white[2]
    board[7][5] = white[2]
    

    #add the royals
    board[0][3] = black[1]
    board[0][4] = black[0]
    board[7][3] = white[1]
    board[7][4] = white[0]
    
    
    return print_grid(board)

def init_board():
    """" 
    This function takes no inputs and returns an empty 8x8 grid 
    that is the empty chess board (with no pieces yet).
    
    """
    board = [["__" for j in range(board_dim)] for i in range(board_dim)]
    return board


intro()
start_board(init_board())
