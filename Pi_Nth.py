# Author: John Ciulla
# Date: 11/17/2023
# Purpose: Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
import subprocess
import sys
from mpmath import mp

# Creates a variable for storing user input
userInput = input("Enter the number of places you'd like to count to Pi in: ")

# Setting up some try/except/else so we can check if the input is an integer
try:
    userInput = int(userInput)
except ValueError:
    print(f"Silly goose, '{userInput}' isn't a number!")
    # This restarts the Python script by getting the path of the interpretter currently running, creating a new process, and starts again
    subprocess.call([sys.executable] + sys.argv)
# The else only hits if the try is successful
else:
    print(f"Your entered number is '{userInput}'")
    # Lets check to see what the last number of the input is so we can do the st, nd, rd, or th at the end of a number
    if userInput % 10 == 1:
        placement = "st"
    elif userInput % 10 == 2:
        placement = "nd"
    elif userInput % 10 == 3:
        placement = "rd"
    else:
        placement = "th"
    # Add two to the number the put because mp.pi rounds it so we want to give an extra number to strip later. Also, we are saying Pi to the nth place
    # and the mp.pi accounts for the first number which is '3'
    mp.dps = userInput + 2
    result = str(mp.pi)
    print(f"Pi to the {userInput}{placement} place is", result[:-1])
