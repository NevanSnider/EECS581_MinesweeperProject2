# Author: Katie Nordberg
# Description: This python scripts includes all te logic to play a game of minesweeper.
# Creation Date: 8/27/2025

# For a 3x3 game board, the board variable will be initialized as:
# [[-1, -1, -1],
#  [-1, -1, -1],
#  [-1, -1, -1]]

# An example of a fully defined 3x3 board where there is only 1 mine and it is in the middle cell would be:
# board = [[1,  1, 1],
#          [1, -1, 1],
#          [1,  1, 1]]

# An example of a fully defined 3x3 board where there are 2 mines (shown by -1s):
# board = [[-1,  2, 1],
#          [ 2, -1, 1],
#          [ 1,  1, 1]]
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
    
# Class Name: BoardManager
# Description: Class to handle all parameters and functions of the game board including
#   - retrieving a cell's mine status (either it contains a mine or it doesnt) {function}
#   - retrieving a cell's visible status (either covered, flagged, or uncovered) {function}
#   - flagging/unflagging a cell {function}
#   - uncovering a cell {function}
#   - displaying the game board {function}
class BoardManager:
    # Class Attributes
    # These are inherent to the board and do not change during the game
    # The number of rows, columns, and mines are set when the board is initialized
    rows = 0
    cols = 0
    mines = 0

    # Attribute Name: boardContent 
    # Description: a 2D array that is accessed as boardContent[i][j] where i is the row and j is the column.
    # Each spot in the matrix holds a number representing the number of mines adjacent to that cell.
    # - If that cell is a mine, it holds a -1.
    # - If that cell is not adjacent to any mines, it holds a 0.
    # Note: After the mines are placed, this list will not change
    boardContent = []

    # Attribute Name: boardState
    # Description: a 2D array that is accessed as boardState[i][j] where i is the row and j is the column.
    # Each spot in the matrix holds a number representing the visible state of that cell.
    # - 0 for covered cells
    # - 1 for flagged cells
    # - 2 for uncovered cells
    # Note: This list will change as the user plays the game
    boardState = []

    # Constructor
    def __init__(self, rows, cols, mines): 
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self._initializeBoard()
    
    # Private Methods

    # Method Name: _initializeBoard
    # Description: This method initializes the game board to be a 2D array of -1s
    # Once the first cell is uncovered, the mines will be placed and the board will be fully defined
    # Input: None (the BoardManager.rows and BoardManager.cols attributes are used)
    # Output: None (BoardManager.board is initialized)
    def _initializeBoard(self):
        self.boardContent = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

        # To start the game, all cells are covered and none are flagged
        self.boardState = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    # Public Methods

    # Method Name: isMine
    # Description: This method checks if a given cell contains a mine
    # Input:
    #   row (int) - the row of the cell to check
    #   col (int) - the column of the cell to check
    # Output:
    #   (bool) - True if the cell contains a mine, False otherwise
    def isMine(self, row, col):
        if self.boardContent[row][col] == -1:
            return True
        else:
            return False
    
    # Method Name: isCovered
    # Description: This method checks if a given cell is covered
    # Input:
    #   row (int) - the row of the cell to check
    #   col (int) - the column of the cell to check
    # Output:
    #   (bool) - True if the cell is covered, False otherwise
    def isCovered(self, row, col):
        if self.boardState[row][col] == 0:
            return True
        else:
            return False
        
    # Method Name: isFlagged
    # Description: This method checks if a given cell is flagged
    # Input:
    #   row (int) - the row of the cell to check
    #   col (int) - the column of the cell to check
    # Output:
    #   (bool) - True if the cell is flagged, False otherwise
    def isFlagged(self, row, col):
        if self.boardState[row][col] == 1:
            return True
        else:
            return False
        
    # Method Name: isUncovered
    # Description: This method checks if a given cell is uncovered
    # Input:
    #   row (int) - the row of the cell to check
    #   col (int) - the column of the cell to check
    # Output:
    #   (bool) - True if the cell is uncovered, False otherwise
    def isUncovered(self, row, col):
        if self.boardState[row][col] == 2:
            return True
        else:
            return False
    
    # Method Name: showBoardContents
    # Description: This method prints the current state of the board to the console
    # Input: None
    # Output: The board is printed to the console
    def showBoardContents(self):
        for row in self.boardContent:
            print(row)
    
    # Method Name: showBoardState
    # Description: This method prints the current visible state of the board to the console
    # Input: None
    # Output: The state of each cell is printed. 
    # - Covered cells display " "
    # - Flagged cells display "F"
    # - Uncovered cells show their content (the number of mines in adjacent cells) unless they are mines, in which case they display "X"
    def showBoardState(self):
        # This way of printing the columns and rows is a bit janky. But it works for grids up to 10x10 which is the max size of the board for this game. Plus we are going to use tkinter for the GUI anyways. 
        print("   " + " ".join([str(i) for i in range(self.cols)])) # Print the columns at the top of the board
        for row in range(self.rows):
            print(f"{row}|", end=" ") # Print the left border of the board
            # For each cell in the row, print the appropriate string based on its state (covered, flagged, or uncovered)
            for col in range(self.cols):
                if self.isCovered(row, col):
                    print(" ", end=" ")
                elif self.isFlagged(row, col):
                    print("F", end=" ")
                elif self.isUncovered(row, col):
                    if self.isMine(row, col):
                        print("X", end=" ")
                    else:
                        print(self.boardContent[row][col], end=" ")
                else:
                    print("?", end=" ") # Something has gone wrong if this prints in any of the cells
            print("|") # Print the right border of the board and a newline

    # Method Name: flagCell
    # Description: This method flags a given cell if it is covered, or unflags it if it is already flagged
    # Input:
    #   row (int) - the row of the cell to flag/unflag
    #   col (int) - the column of the cell to flag/unflag
    # Output: The BoardManager.boardState attribute is updated
    def flagCell(self, row, col):
        # If the cell is covered, flag it
        if self.isCovered(row, col):
            self.boardState[row][col] = 1
        # If the cell is already flagged, unflag it
        elif self.isFlagged(row, col):
            self.boardState[row][col] = 0
        # If the cell is uncovered, do nothing
        else:
            print("Cell is already uncovered. Cannot flag an uncovered cell.")
    
    # Method Name: uncoverCell
    # Description: This method uncovers a given cell (only if it is covered)
    # Input:
    #   row (int) - the row of the cell to uncover
    #   col (int) - the column of the cell to uncover
    # Output: The BoardManager.boardState attribute is updated
    def uncoverCell(self, row, col):
        # If the cell is covered, uncover it)
        if self.isCovered(row, col):
            self.boardState[row][col] = 2
            
        # If the cell is already uncovered or if it is flagged, do nothing
        else:
            print("Cell is already uncovered or flagged. Cannot uncover this cell.")

    # At the beginning of the game, all cells are initialized to -1.
    # The placement of the mines is not assigned until after the first cell is uncovered.
    # This ensures that the first cell uncovered is never a mine.

    # The board will be fully defined as soon as the game starts (as soon as the first cell is uncovered).

# Function Name: validatedIntInputInRange
# Description: This helper function ensures that the inputted text is an integer within the valid range.
# It will continue prompting the user for correct input until it is satisfied. 
# Input:
#   min_val (int) - the minimum valid value (inclusive)
#   max_val (int) - the maximum valid value (inclusive)
#   message (str) - the message to display to the user when prompting for input
# Output:
#   Returns an int - the validated integer input that is within the specified range
def validatedIntInputInRange(min_val, max_val, message):
    while True:
        try:
            value = int(input(f"{message.strip()} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Must be between {min_val} and {max_val}!")
        except ValueError:
            print(f"Invalid input. Please enter an integer between {min_val} and {max_val}.")

if __name__ == "__main__":
    print("Welcome to Minesweeper!")
    numMines = validatedIntInputInRange(10, 20, "Enter the number of mines")
    # game = BoardManager(10, 10, numMines)
    # game.showBoardState()

    # This is an example of a hardcoded boardContent for testing purposes.
    sample = BoardManager(10, 10, 10)
    sample.boardContent = sampleBoard10Mines # This is just for testing purposes. The mines would normally be placed after the first cell is uncovered.
    sample.showBoardState()
    playing = True

    # Game loop
    while playing:
        # Prompt user for what action to take
        action = input("Enter 'f' to flag/unflag a cell, 'u' to uncover a cell, or 'q' to quit: ")
        # Flag/unflag a cell and show the updated board state
        if action == 'f':
            row = validatedIntInputInRange(0, sample.rows - 1, "Row")
            col = validatedIntInputInRange(0, sample.cols - 1, "Column")
            sample.flagCell(row, col)
            sample.showBoardState()
        # Uncover a cell and show the updated board state
        elif action == 'u':
            row = validatedIntInputInRange(0, sample.rows - 1, "Row")
            col = validatedIntInputInRange(0, sample.cols - 1, "Column")
            sample.uncoverCell(row, col)
            sample.showBoardState()

            # If the uncovered cell is a mine, end the game
            if not sample.isFlagged(row, col) and sample.isMine(row, col):
                print("BOOM! Game Over.")
                playing = False # End the game loop
        # Quit game
        elif action == 'q':
            print("Thanks for playing!")
            playing = False # End the game loop
        # When the user enters something other than f, u, or q
        else:
            print("Invalid input. Please try again.")