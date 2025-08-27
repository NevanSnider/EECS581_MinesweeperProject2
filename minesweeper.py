# Author: Katie Nordberg
# Description: This python scripts includes all te logic to play a game of minesweeper.
# Creation Date: 8/27/2025

# For a 3x3 game board, the board variable will be initialized as:
# [[-1, -1, -1],
#  [-1, -1, -1],
#  [-1, -1, -1]]

# An example of a fully defined 3x3 board where there is only 1 mine and it is in the middle cell would be:
# board =           [[1,  1, 1],
#                    [1, -1, 1],
#                    [1,  1, 1]]

# An example of a fully defined 3x3 board where there are 2 mines (shown by -1s):
# board =           [[-1,  2, 1],
#                    [ 2, -1, 1],
#                    [ 1,  1, 1]]
# board[0][0] and board[1][1] have mines because they are -1

# mines = [(0,0), (1, 3), (2, 7), (3, 7), (4, 7), (5, 1), (7, 4), (7,5), (8,2), (9,9)]
# Note: I made this by hand for testing purposes. I believe I got each cell right, but I could have miscalculated somewhere. Let me know if you see any errors! - Katie
sampleBoard10Mines =   [[-1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                        [ 1, 1, 1,-1, 1, 0, 1, 1, 1, 0],
                        [ 0, 0, 1, 1, 1, 0, 1,-1, 2, 1],
                        [ 0, 0, 0, 0, 0, 0, 1, 3,-1, 2],
                        [ 1, 1, 1, 0, 0, 0, 0, 2,-1, 2],
                        [ 1,-1, 1, 0, 0, 0, 0, 1, 1, 1],
                        [ 1, 1, 1, 1, 2, 1, 1, 0, 0, 0],
                        [ 0, 1, 1, 2,-1,-1, 1, 0, 0, 0],
                        [ 0, 1,-1, 2, 2, 2, 1, 0, 1, 1],
                        [ 0, 1, 1, 1, 0, 0, 0, 0, 1,-1]]

# Function Name: Minesweeper
# Description: Start a game of minesweeper
# Input: 
#   rows (int) - the number of rows in the game board
#   cols (int) - the number of columns in the game board
# TODO: change this when there is output
# Output: None
def Minesweeper(rows, cols):
    # The game board is a 2D array that is accessed as board[i][j] where i is the row and j is the column.
    # Each spot in the matrix holds a number representing the number of mines adjacent to that cell.
    # If that cell is a mine, it holds a -1.
    # If that cell is not adjacent to any mines, it holds a 0.
    # At the beginning of the game, all cells are initialized to -1.
    # The placement of the mines is not assigned until after the first cell is uncovered.
    # This ensures that the first cell uncovered is never a mine.
    board = [[-1 for _ in range(cols)] for _ in range(rows)] 

    # The board will be fully defined as soon as the game starts (as soon as the first cell is uncovered).
    # The locations of the mines are represented by a -1 in the board variable. 


    # TODO: delete this print statement when tkinter is implemented
    for row in board:
        print(row)
    
if __name__ == "__main__":
    game = Minesweeper(10, 10)