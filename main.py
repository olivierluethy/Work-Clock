# Import modules
import time
import datetime
import os

# Define a function to show notification
def show_notification(title, message):
    # Play alert sound
    os.system('powershell -c "(New-Object Media.SoundPlayer \'C:\Windows\Media\Speech On.wav\').PlaySync()"')

    # Show notification
    os.system(f"powershell -c \"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;\
                $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);\
                $xml = $template.GetXml();\
                $toast = [xml]::new($xml.OuterXml);\
                $toast.SelectNodes('//toast')[0].SetAttribute('duration','long');\
                $toast.SelectNodes('//text')[0].AppendChild($toast.CreateTextNode('{title}'));\
                $toast.SelectNodes('//text')[1].AppendChild($toast.CreateTextNode('{message}'));\
                [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Reminder').Show($toast);\"")

# Define a list of times to notify
notify_times = ["10:00", "12:00", "15:00", "17:50"]

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
