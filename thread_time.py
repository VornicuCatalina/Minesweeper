import time

import threading
import global_variables_file

# I might need a global variable for time_seconds that is not the default one because this one will keep
# on getting subtracted by 1 as time passes
time_seconds_for_this_game = 120

# to check if the window still exists
still_exist = True
# or if I left the game
left_the_game = False

# for when playing the game : -1 lost 1 won 0 not knowing
winning_or_losing = 0


# used when we close the window via X button in the top right corner
def on_close(root):
    global still_exist
    still_exist = False
    root.destroy()


# counting the time -> chronometer
def counting_down_time(used_label):
    global time_seconds_for_this_game, winning_or_losing
    time_seconds_for_this_game = global_variables_file.time_seconds
    while time_seconds_for_this_game > 0 and still_exist and not left_the_game and winning_or_losing == 0:
        show_time = show_current_time(time_seconds_for_this_game)
        used_label.config(text=str(show_time))
        time.sleep(1)
        time_seconds_for_this_game -= 1
        if time_seconds_for_this_game == 0:
            winning_or_losing = -1
    if winning_or_losing == 1:
        used_label.config(text="You won!")
    elif winning_or_losing == -1:
        used_label.config(text="You lost!")


# the function that creates the thread and calls it
def calling_the_thread_for_time(used_label, root):
    thread = threading.Thread(target=lambda: counting_down_time(used_label))
    thread.start()
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))


# to convert the seconds into minutes & seconds: chronometer model
def show_current_time(variable_time):
    minutes = variable_time // 60
    seconds = variable_time % 60
    if seconds < 10:
        show_time = str(minutes) + ":0" + str(seconds)
    else:
        show_time = str(minutes) + ":" + str(seconds)
    return show_time
