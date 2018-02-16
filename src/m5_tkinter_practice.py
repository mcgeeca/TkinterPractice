"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Craig McGee Jr.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()  # makes a window
    print('Done with the Event Loop')  # Note when this line runs.
    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()  # similar to window.render
    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    go_forward_button = ttk.Button(frame1, text = 'Say Hello')
    go_forward_button.grid()
    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    go_forward_button['command'] = (lambda:
                                     print_hello())
    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1, width = 10)
    my_entry_box.grid()

    hello_goodbye_button = ttk.Button(frame1, text = "Test for ok")
    hello_goodbye_button["command"] = lambda:check_for_ok(my_entry_box)
    hello_goodbye_button.grid()

    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    my_second_entry_box = ttk.Entry(frame1, width=10)
    my_second_entry_box.grid()
    my_third_button = ttk.Button(frame1, text="Print string N times")
    my_third_button["command"] = lambda: printed_n_times(my_entry_box, my_second_entry_box)
    my_third_button.grid()
    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()  # infinite while loop goes until the program is closed


def print_hello():
    print("hello")


def check_for_ok(entry_box):
    contents = entry_box.get()
    if contents == "ok":
        print("Hello")
    else:
        print("Goodbye")


def printed_n_times(entry_box, my_second_entry_box):
    s = entry_box.get()
    n = int(my_second_entry_box.get())
    print(n*s)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
