board_dim = 8

# a dictionary used when labelling the columns of the board
letters = {0: "a", 1: "b",  2: "c", 3: "d", 4: "e", 5: "f",  6: "g", 7: "h"} 

#changes the keys in letters to the values for use in moving the chess pieces
lets_to_nums = {val: key for key, val in letters.items()}
    

#contains the chessmen for each player
white = {0: "♔", 1: "♕", 2: "♗", 3: "♖", 4: "♘", 5: "♙"}    
black = {0: "♚", 1: "♛", 2:"♝", 3: "♜", 4: "♞", 5: "♟︎"}


def intro():
    print("Welcome to my chess game!")
    print()
    print("The player with the white pieces is to go first.")
    print()
    print(f"Valid row numbers to enter are 1 to 8.")
    print(f"Valid column labels to enter are a,b,c,d,e,f,g or h")

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
        print(letters[i], end = "\t")
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



def main():
    user_turn = "white" # white pieces start the game
    intro()
    board = init_board()
    start_board(board)
    
    while True:
        print()
        print(f"It is currently {user_turn}'s move. Good luck!")
        print_grid(board)
        print()
        
        #this is a number
        piece_row = int(input("Enter the row of the chessman you want to move: "))
    
        #this is a letter
        piece_col_a = input("Enter the column of the chessman you want to move: ")
        
        #converts to number
        piece_col = int(lets_to_nums[piece_col_a])
    
        
        
        # this is a number
        move_row = int(input("Enter the row that you want to move your chessman to: "))
        
        # this is a letter
        move_col_a = input("Enter the column that you want to move your chessman to: ")
        
        # converts to a number
        move_col = int(lets_to_nums[move_col_a])
        
        
        #ensure the move the player wants to make is allowed
        if error(board, move_row, move_col, user_turn, piece_row, piece_col) == False and path_clear(piece_row, move_row, board, piece_col, move_col):
                #displays updated board
                print_grid(board)
                # this moves the piece to where the user wants 
                # first the inputted row number must be converted to the actual index
                board[8 - move_row][move_col] = board[8 - piece_row][piece_col]
       
                # this replaces the moved piece with a blank space 
                # first the inputted row number must be converted to the actual index
                board[8 - piece_row][piece_col] = "__"
                
                # alternates player turns
                if user_turn == "white":
                    user_turn = "black"
            
                else:
                    user_turn = "white"
        else:
            print("Sorry that is not a valid move")
                    

def error(board, move_row, move_col, user_turn, piece_row, piece_col):
    """this function will return True if a user places their piece onto 
    another one of their pieces"""
    
    if board[8 - move_row][move_col] in white.values() and board[8 - piece_row][piece_col] in white.values():
        return True
            
    elif board[8 - move_row][move_col] in black.values() and board[8 - piece_col][piece_col] in black.values():
        return True
    
    return False

def path_clear(piece_row, move_row, board, piece_col, move_col):
    """
    This function returns TRUE if the path between the chessman's current position
    and the one it wants to move to is clear.
    
    CAUTION this only works for checking that a horizontal or vertical path is clear
    
    """
    # checks vertical path
    if piece_row < move_row:
        rows = [i for i in range(piece_row + 1, move_row + 1)]
    else:
        rows = [i for i in range(move_row + 1, piece_row + 1)]
    for row in rows:
        if board[8-row][move_col] != "__":            
            return False
        
    return True
    


def rooks(board, move_row, move_col, user_turn, piece_row, piece_col):
    """
    This function returns False if the player wants to move their rook
    to an invalid position and True otherwise
    
    """
    # check that the rook can't jump over existing pieces
    if path_clear(piece_row, move_row, board, piece_col, move_col) == False:
        return False
    
    else:
    # check that the rook only moves horizontally or vertically
         if board[8 - piece_row]== board[8 - move_row]:
             return  True
    
         elif board[piece_col]== board[move_col]:
             return True
       
         else:
            return False
    

def check_valid(board, move_row, move_col, user_turn,piece_row, piece_col):
    """
    This is a function that returns true if the user's moves are allowed
    according to the rules of chess.
    
    """
    
    
    
    


if __name__ == "__main__":
    main()