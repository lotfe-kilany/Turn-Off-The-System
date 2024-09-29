import os
import time
import platform

# Version of the script
version = "1.0.0"

# Print the version to the user
print(f"Script version: {version}")

# Function to shutdown the system
def shutdown_system():
    system_name = platform.system()
    if system_name == "Windows":
        os.system("shutdown /s /f /t 60")  # Shutdown with a 60-second delay for data saving
    elif system_name == "Linux" or system_name == "Darwin":  # Darwin is macOS
        os.system("sudo shutdown -h +1")  # Shutdown with a 1-minute delay
    else:
        print(f"Unsupported OS: {system_name}")
        exit()

# Request shutdown time from the user (in minutes)
shutdown_time = input("Enter the number of minutes before shutdown: ")

# Validate that the input is a valid integer
try:
    shutdown_time_seconds = int(shutdown_time) * 60
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Wait for the specified time before notifying
time.sleep(shutdown_time_seconds)

# Notify user to save their work
input("Time's up! Please save your work. Press Enter to continue with the shutdown...")

# Wait for user confirmation to shutdown
confirm = input("Do you want to proceed with the shutdown? (yes/no): ").strip().lower()
if confirm == "yes":
    shutdown_system()  # Proceed with shutdown
else:
    print("Shutdown canceled.")
    exit()
