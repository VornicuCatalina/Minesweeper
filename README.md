# Minesweeper

Python project

# Rules for my project:

1. The time will be chosen in seconds
2. When the user marks the empty cell as bomb when it is not and clicks after on a connected cell to it, the cells that
   will be shown to the user will not include the cell marked as bomb even if it is an empty cell

# What files contains

1. main
   * here it is included the graphical part for each menu and subsection: game, settings and how the game is exited
   * it also builds the settings (graphical part)
   * the game -> its matrix and visual part, calls the other files as much as needed
2. global_variables_file
   * global variables that are used almost in all files: variables for the game, window size, what type of button we use
   * global functions: the one for clearing the wedges and the one for updating the values for the global variables for the game
3. start_game
   * functions for the back-end matrices: solution (what the solution should be), user (the current state of the game)
   * how the bombs are placed
   * how to reveal the neighbors of an empty cell when found
4. thread_time
   * creating the thread for the chronometer in the game
   * the converter for time (min & sec)
   * the used protocol when the window is closed accidentally or if wanted ? -> so the thread will stop
5. classes_cell_and_minesweeper
   * cell class: each cell of the class minesweeper
     + includes the variables needed for a cell: if it is a bomb, it is revealed, row, column and so on
     + the function when it is clicked which is divided into 2: when the flag button is on, otherwise bomb button is on; also calls the function for checking if the user on (other class function)
     + when flag button is on: checks for 2 cases when it is not marked as a bomb or when it is; also checks if it is revealed
     + when bomb button is on: checks if the cell is a bomb -> ends the game || if the cell is a number -> reveals it || the cell is empty -> class the function from the other class to reveal all its neighbors without the ones who have a flag on
   * minesweeper class: contains all cells, acts as a matrix
     + includes the variables needed for the matrix: number cols, rows, the array of cells and so on
     + the function when the game is finished -> tells the user if he won or lost based on the time & if a bomb was clicked on
     + the function that checks if the solution was found after each click
     + and the function that shows the complete solution to the user: reveals the cells and marks with 'X' the wrong flagged cells