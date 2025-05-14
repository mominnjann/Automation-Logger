# Automation Logger

**Owner:** Momin Jan

## Overview

Automation Logger is a simple Python tool that uses a GUI (built with Tkinter) to automate sending messages to any application. It leverages `pyautogui` to simulate keyboard input, making it easy to send repeated messages with custom delays.

## Features

- **Custom Message:** Enter any message to be sent.
- **Delay:** Set the delay (in seconds) between each message.
- **Count:** Specify how many times the message should be sent.
- **Start/Stop:** Start or stop the automation at any time.
- **5-Second Preparation:** After clicking "Send Message," you have 5 seconds to switch to your target application before the first message is sent.

## Supported Platforms

- **Windows:** Fully supported and tested.
- **macOS:** Supported (some hotkeys or automation features may behave differently).
- **Linux:** Supported (ensure your desktop environment allows simulated keyboard input).

> **Note:** Some applications or operating systems may restrict automated input for security reasons. Always test in your environment.

## Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/)
- Tkinter (comes with most Python installations)

## Installation

1. Clone or download this repository.
2. Install `pyautogui` if you haven't already:
    ```
    pip install pyautogui
    ```

## Usage

1. Run the GUI:
    ```
    python gui.py
    ```
2. Enter your message, delay, and count.
3. Click **Send Message**.
4. Switch to your target application within 5 seconds (the first message will be sent after this delay).
5. To stop sending messages, click **Stop**.

## Notes

- Make sure the target application is focused and ready to receive input.
- Use responsibly. Automation scripts can cause unintended actions if misused.
- Some applications may block automated input for security reasons.
- Always test in a safe environment before using in critical applications.

## File Structure

```
gui.py           # Main GUI application
main.py          # Simple script version (no GUI)
README.md        # This file
requirements.txt # Python dependencies
```

---

**Created by Momin Jan**