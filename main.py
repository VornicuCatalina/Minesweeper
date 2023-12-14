import global_variables_file
import tkinter as tk

# the root of the project aka the window
root = tk.Tk()
# Set the window title to "Minesweeper"
root.title("Minesweeper")


def get_window_size():
    global_variables_file.window_height = root.winfo_screenheight()
    global_variables_file.window_width = root.winfo_screenwidth()

    # Set the window size to match the screen size
    root.geometry(f"{global_variables_file.window_width}x{global_variables_file.window_height}")

    # modifying the icon
    root.iconbitmap("./pictures/icon_game.ico")


def on_start():
    print("Starting a new game!")


def on_settings():
    print("The settings come")


def on_exit():
    print("Exiting the application")
    root.destroy()


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
    get_window_size()
    creating_the_menu()
    root.mainloop()


main_prog()
# click on start

# click on settings

# click on exit
