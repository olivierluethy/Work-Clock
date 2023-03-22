# Work Clock Notification System
This Python script provides a notification system that reminds the user of certain events during the day based on the time of day.

The script uses the datetime and time modules to check the current time and a list of times to notify. If the current time matches any of the times in the list, a notification is displayed using the win10toast library.

The notification messages are customized based on the time of day. For example, if the current time is 12:00, the notification message will remind the user to take a lunch break.

## How to Use
Install the win10toast library by running the command pip install win10toast in your terminal.

Copy the code to a Python file on your local machine.

Modify the notify_times list to include the times you want to receive notifications.

Customize the show_notification function to display the notification message you want for each time of day.

Run the script in your terminal using the command python work_clock.py.

## Notification Messages
The notification messages are customized based on the time of day. Here are the messages that are displayed for each time of day:

12:00: "Es ist Mittagszeit!\nZeit zum Essen" (It's lunchtime! Time to eat)<br>
10:00 and 15:00: "Bereit für 15 Minuten Pause\nGeh, und hol dir frische Luft!" (Ready for a 15-minute break? Go and get some fresh air!)<br>
16:50: "You are finished for today!\nCongrats" (You are finished for today! Congratulations)<br>
Note that you can customize these messages by modifying the show_notification function in the code.<br>
