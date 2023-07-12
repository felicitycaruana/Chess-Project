board_dim = 8
letters = {0: "a", 1: "b",  2: "c", 3: "d", 4: "e", 5: "f",  6: "g", 7: "h"} 
    #letters is a dictionary used when labelling the columns of the board

lets_to_nums = {val: key for key, val in letters.items()}
    #a dictionary that changes the keys in letters to the values
        #for use in moving the chess pieces

#white and black are dictionaries containing the chessmen for each player
white = {0: "♔", 1: "♕", 2: "♗", 3: "♖", 4: "♘", 5: "♙"}    
black = {0: "♚", 1: "♛", 2:"♝", 3: "♜", 4: "♞", 5: "♟︎"}

# this line is for usability in dark mode so the pieces are the correct colour
white, black = black, white


def intro():
    print("Welcome to my chess game!")
    print()
    print("The player with the white pieces is to go first.")
    print()
    print(f"Valid row numbers to enter are 1 to 8.")
    print(f"Valid column labels to enter are a,b,c,d,e,f,g or h")
    
    #ADD INSTRUCTIONS ON HOW TO PLAY
    
    
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
    user_turn = "white" 
    intro()
    board = init_board()
    start_board(board)
    
    while True: ## CAUTION THIS IS CURRENTLY AN ENDLESS LOOP ##
        print()
        print(f"It is currently {user_turn}'s move. Good luck!")
        print()
        
        
        piece_row = int(input("Enter the row of the chessman you want to move: "))
        # this is a number
        
        piece_col_a = input("Enter the column of the chessman you want to move: ")
        # this is a letter
        
        piece_col = int(lets_to_nums[piece_col_a])
        # this is now a number
        
        
        
        move_row = int(input("Enter the row that you want to move your chessman to: "))
        # this is a number
        
        move_col_a = input("Enter the column that you want to move your chessman to: ")
        # this is a letter
        
        move_col = int(lets_to_nums[move_col_a])
        # this is now a number
        
        
        
        
        
        
        # check that we have correctly identified hte piece we want to move
        print(f"The piece you want to move is {board[8 - piece_row][8 - piece_col]}")
        
        board[8 - move_row][8 - move_col] = board[8 - piece_row][8 - piece_col]
        board[8 - piece_row][8 - piece_col] = "__"
        
        
        print_grid(board)
        
       
        break
        
        
        
        









if __name__ == "__main__":
    main()