import tkinter as tk
import random

# global variables used in the whole project
# the game will use the default values in case that they will not be modified
height = 10
width = 10
number_bombs = 10
time_seconds = 120

# window size
window_height = 0
window_width = 0

# the bombs will be checked first
is_looking_for_bombs = True

# the root of the project aka the window
root = tk.Tk()

# Set the window title to "Minesweeper"
root.title("Minesweeper")


# global functions
def clear_widgets():
    # Destroy all widgets in the current window
    for widget in root.winfo_children():
        widget.destroy()


def get_window_size():
    global window_height, window_width
    window_height = root.winfo_screenheight()
    window_width = root.winfo_screenwidth()

    # Set the window size to match the screen size
    root.geometry(f"{window_width}x{window_height}")

    # modifying the icon
    root.iconbitmap("./pictures/icon_game.ico")


def update_label(height_entry, height_label, width_entry, width_label, bombs_entry, bombs_label, time_entry,
                 time_label):
    global height, width, number_bombs, time_seconds
    try:
        current_var = height_entry.get()
        current_var_int = int(current_var)
        if 30 > current_var_int > 2:
            height = current_var_int
            height_label.config(text=f"Height number = {height}")
        else:
            print("Not an accepted height")
    except ValueError:
        print("An invalid type for height")

    try:
        current_var = width_entry.get()
        current_var_int = int(current_var)
        if 45 > current_var_int > 2:
            width = current_var_int
            width_label.config(text=f"Width number = {width}")
        else:
            print("Not an accepted width")
    except ValueError:
        print("An invalid type for width")

    try:
        current_var = bombs_entry.get()
        current_var_int = int(current_var)
        if current_var_int > height * width or current_var_int < 1:
            number_bombs = random.randint(height * width // 4, 3 * height * width // 4)
            bombs_label.config(text=f"Bombs number = {number_bombs}")
        elif current_var_int > 1:
            number_bombs = current_var_int
            bombs_label.config(text=f"Bombs number = {number_bombs}")
    except ValueError:
        print("An invalid type for number of bombs")

    try:
        current_var = time_entry.get()
        current_var_int = int(current_var)
        if 1800 >= current_var_int > 10:
            time_seconds = current_var_int
            time_label.config(text=f"Time = {time_seconds}")
        else:
            print("Not accepted number seconds value")
    except ValueError:
        print("An invalid type for chronometer")
