import time
import datetime
import os
import win10toast

# Define a function to show notification
def show_notification(title, message):
    # Create a ToastNotifier object
    toaster = win10toast.ToastNotifier()

    if title == "12:00":
        result = "Es ist Mittagszeit!\nZeit zum Essen"
    elif title == "10:00" and title == "15:00":
        result = "Bereit für 15 Minuten Pause\nGeh, und hol dir frische Luft!"
    elif title == "22:02":
        result = "You are finished for today!\nCongrats"

    # Show notification
    toaster.show_toast(result, title, message, duration=15, threaded=True)

# Define a list of times to notify
notify_times = ["22:02", "12:00", "15:00", "17:50"]

# Loop forever
while True:
    # Get the current time as a string in HH:MM format
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Check if the current time is in the notify times list
    if current_time in notify_times:
        # Show a notification with the current time as the title and message
        show_notification(current_time, current_time)

        # Wait for one minute to avoid repeating notifications for the same time
        time.sleep(60)
    
    # Wait for one second before checking again
    time.sleep(1)
