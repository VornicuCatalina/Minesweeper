import tkinter as tk
import global_variables_file
import thread_time
from global_variables_file import root
import start_game
import classes_cell_and_minesweeper


# functions for buttons
def on_start():
    """
    clearing the widgets whenever we click on the back button (to go back to a specific window - usually menu one)
    calls the function of the graphical part of the game

    :return: nothing (void function)
    """
    global_variables_file.clear_widgets()
    playing_game()


def on_settings():
    """
    clearing the widgets whenever we click on the back button (to go back to a specific window - usually menu one)
    calls the function of the graphical part of the settings

    :return: nothing (void function)
    """
    global_variables_file.clear_widgets()
    options()


def on_exit():
    """
    destroys the root of the app

    :return: nothing (void function)
    """
    root.destroy()


def back_on_menu():
    """
    clearing the widgets whenever we click on the back button (to go back to a specific window - usually menu one)
    tells the thread to stop counting down because the player left the game (for not getting error when leaving a game
    suddenly)
    recreates the graphics of the menu

    :return: nothing (void function)
    """
    global_variables_file.clear_widgets()
    thread_time.left_the_game = True
    creating_the_menu()


# menu
def creating_the_menu():
    """
    The graphical part of the menu and its buttons

    :return: nothing (void function)
    """
    # Add a label to the window
    button_start = tk.Button(root, text="Start", relief=tk.FLAT, cursor="hand2", command=on_start)
    button_settings = tk.Button(root, text="Settings", relief=tk.FLAT, cursor="hand2", command=on_settings)
    button_exit = tk.Button(root, text="Exit", relief=tk.FLAT, cursor="hand2", command=on_exit)

    # packing_them
    button_start.pack()
    button_settings.pack()
    button_exit.pack()


def main_prog():
    """
    To display the width and height of the windows of the application and calls the main menu function

    :return: nothing (void function)
    """
    global_variables_file.get_window_size()
    creating_the_menu()


# settings
def options():
    """
    It displays the GUI of the settings window

    :return: nothing (void function)
    """
    settings_label = tk.Label(root, text="SETTINGS")
    settings_label.grid(row=0, sticky="ew")

    # height
    height_label = tk.Label(root, text=f"Height number = {global_variables_file.height}")
    height_label.grid(row=1, column=0, sticky="w")
    height_entry = tk.Entry(root)
    height_entry.grid(row=1, column=1)

    # width
    width_label = tk.Label(root, text=f"Width number = {global_variables_file.width}")
    width_label.grid(row=2, column=0, sticky="w")
    width_entry = tk.Entry(root)
    width_entry.grid(row=2, column=1)

    # bombs
    number_bombs_label = tk.Label(root, text=f"Bombs number = {global_variables_file.number_bombs}")
    number_bombs_label.grid(row=3, column=0, sticky="w")
    number_bombs_entry = tk.Entry(root)
    number_bombs_entry.grid(row=3, column=1)

    # time
    time_seconds_label = tk.Label(root, text=f"Time = {global_variables_file.time_seconds}")
    time_seconds_label.grid(row=4, column=0, sticky="w")
    time_seconds_entry = tk.Entry(root)
    time_seconds_entry.grid(row=4, column=1)

    # Create a button to get back to the menu
    back_button = tk.Button(root, text="Back", command=back_on_menu)
    back_button.grid(row=5, column=0, columnspan=2)

    # Create a button to update the label
    update_button = tk.Button(root, text="Update",
                              command=lambda: global_variables_file.update_label(height_entry, height_label,
                                                                                 width_entry, width_label,
                                                                                 number_bombs_entry, number_bombs_label,
                                                                                 time_seconds_entry,
                                                                                 time_seconds_label))
    update_button.grid(row=5, column=3, columnspan=2)


# the game
def playing_game():
    """
    This function is used to display the graphics of the game and also restores the variables every single time when
    the game is replayed

    :return: nothing (void function)
    """
    # returning to default values used in the thread
    thread_time.left_the_game = False
    thread_time.winning_or_losing = 0

    # default value for the buttons
    global_variables_file.is_looking_for_bombs = True

    # Create a button to get back to the menu
    back_button = tk.Button(root, text="Back", command=back_on_menu)
    back_button.grid(row=0, column=0)

    # buttons for checking one of the 2 options: bombs or putting flags
    bomb_button = tk.Button(root, text="Bomb",
                            command=lambda: start_game.change_is_bomb(True, bomb_button, flag_button), bg="orange")
    bomb_button.grid(row=0, column=3, columnspan=2)

    flag_button = tk.Button(root, text="Flag",
                            command=lambda: start_game.change_is_bomb(False, bomb_button, flag_button), bg="grey")
    flag_button.grid(row=0, column=5, columnspan=2)

    # the timer for the game
    label_time = tk.Label(root, text="")
    label_time.grid(row=0, column=10, columnspan=4)
    thread_time.calling_the_thread_for_time(label_time, root)

    # creating the matrices : solution & user
    [user, solution] = start_game.creating_the_used_matrices_behind(global_variables_file.height,
                                                                    global_variables_file.width,
                                                                    global_variables_file.number_bombs)

    # initialising the cells
    _ = classes_cell_and_minesweeper.Minesweeper(root, solution, user)


# main program
main_prog()
root.mainloop()
