# Import the playsound function from the playsound module
from playsound import playsound
import time  # Import the time module

# ANSI escape sequences for clearing the screen
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to trigger the alarm after a certain number of seconds


def alarm(seconds):
    time_elapsed = 0  # Initialize the time elapsed to 0
    print(CLEAR)  # Clear the screen
    while time_elapsed < seconds:  # Loop until the time elapsed reaches the specified seconds
        time.sleep(1)  # Pause the program for 1 second
        time_elapsed += 1  # Increment the time elapsed by 1 second

        time_left = seconds - time_elapsed  # Calculate the remaining time

        minutes_left = time_left // 60  # Calculate the number of minutes left
        seconds_left = time_left % 60  # Calculate the number of seconds left

        # Print the time left in the format MM:SS
        print(
            f"{CLEAR_AND_RETURN}Alarm with sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.wav")  # Play the alarm sound


# Get the input for the number of minutes and seconds for the alarm
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# Calculate the total number of seconds
total_seconds = minutes * 60 + seconds

# Call the alarm function with the total number of seconds
alarm(total_seconds)
