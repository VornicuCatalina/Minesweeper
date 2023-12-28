import tkinter as tk
import global_variables_file
import thread_time
from global_variables_file import root
import start_game


def on_start():
    global_variables_file.clear_widgets()
    playing_game()


def on_settings():
    global_variables_file.clear_widgets()
    options()


def on_exit():
    root.destroy()


def back_on_menu():
    global_variables_file.clear_widgets()
    thread_time.left_the_game = True
    creating_the_menu()


# menu
def creating_the_menu():
    # Add a label to the window
    button_start = tk.Button(root, text="Start", relief=tk.FLAT, cursor="hand2", command=on_start)
    button_settings = tk.Button(root, text="Settings", relief=tk.FLAT, cursor="hand2", command=on_settings)
    button_exit = tk.Button(root, text="Exit", relief=tk.FLAT, cursor="hand2", command=on_exit)

    # packing_them
    button_start.pack()
    button_settings.pack()
    button_exit.pack()


def main_prog():
    global_variables_file.get_window_size()
    creating_the_menu()


# settings
def options():
    settings_label = tk.Label(root, text="SETTINGS")
    settings_label.grid(row=0, sticky="ew")

    # height
    height_label = tk.Label(root, text=f"Current height number = {global_variables_file.height}")
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
    thread_time.left_the_game = False
    # Create a button to get back to the menu
    back_button = tk.Button(root, text="Back", command=back_on_menu)
    back_button.grid(row=0, column=0)

    # buttons for checking one of the 2 options: bombs or putting flags
    bomb_button = tk.Button(root, text="Choose bomb", command=lambda: start_game.change_is_bomb(True))
    bomb_button.grid(row=0, column=1)

    flag_button = tk.Button(root, text="Choose flag", command=lambda: start_game.change_is_bomb(False))
    flag_button.grid(row=0, column=2)

    # the timer for the game
    label_time = tk.Label(root, text="")
    label_time.grid(row=0, column=10)
    thread_time.calling_the_thread_for_time(label_time, root)


main_prog()
root.mainloop()

# logic functions
