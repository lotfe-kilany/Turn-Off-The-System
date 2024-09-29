Turn Off The System.py

# Turn Off The System

Version: 1.0.0

## Description

This script is a simple tool that allows users to schedule a system shutdown after a specified amount of time. It is compatible with Windows, Linux, and macOS. The user can specify the shutdown delay in minutes, and the script will notify the user to save their work before initiating the shutdown process.

## Features

- Cross-platform support: Windows, Linux, and macOS.
- User-defined shutdown timer (in minutes).
- Notifies the user to save their work before proceeding with the shutdown.
- User confirmation before shutdown.
  
## How It Works

1. The user enters the number of minutes before the system should shut down.
2. The script waits for the specified time.
3. The user is notified to save their work.
4. The user confirms if they want to proceed with the shutdown or cancel it.
5. If confirmed, the system shuts down; otherwise, the shutdown is canceled.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/lotfe-kilany/Turn-Off-The-System.git
    ```

2. Navigate to the script directory:
    ```bash
    cd Turn-Off-The-System
    ```

3. Run the script using Python:
    ```bash
    python Turn-Off-The-System.py
    ```

4. Enter the number of minutes before shutdown, and follow the on-screen instructions.

## Supported Operating Systems

- **Windows**: Uses `shutdown /s /f /t` with a 60-second delay to allow for saving work.
- **Linux/macOS**: Uses `shutdown -h` with a 1-minute delay.

## Requirements

- Python 3.x
- Administrative privileges for system shutdown (e.g., `sudo` for Linux/macOS).

## Notes

- Make sure you have the necessary permissions to perform system shutdowns on your machine.
- You can further enhance the script by adding a graphical user interface or scheduling additional tasks before shutdown.

## License

This project is licensed under the MIT License.
