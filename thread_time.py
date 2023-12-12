import time

import threading
import global_variables_file

# I might need a global variable for time_seconds that is not the default one because this one will keep
# on getting subtracted by 1 as time passes
time_seconds_for_this_game = 120


def counting_down_time():
    global time_seconds_for_this_game
    time_seconds_for_this_game = global_variables_file.time_seconds
    while time_seconds_for_this_game > 0:
        time.sleep(1)
        time_seconds_for_this_game -= 1


def calling_the_thread_for_time():
    thread = threading.Thread(target=counting_down_time())
    thread.start()
    thread.join()


# calling_the_thread_for_time()
