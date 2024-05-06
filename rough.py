import pyautogui
import time

# Move the mouse to coordinates (100, 100) over 1 second
pyautogui.moveTo(100, 100, duration=1)

# Move the mouse relative to its current position
pyautogui.move(50, 50, duration=1)

# Click the left mouse button
pyautogui.click()

# Type a message
pyautogui.typewrite("Hello, PyAutoGUI!")

# Press the Enter key
pyautogui.press("enter")

# Get the screen size
screen_width, screen_height = pyautogui.size()
print("Screen width:", screen_width)
print("Screen height:", screen_height)

# Get the current mouse position
x, y = pyautogui.position()
print("Current mouse position:", x, y)

# Wait for 2 seconds
time.sleep(2)

# Scroll the mouse wheel up
pyautogui.scroll(10)

# Scroll the mouse wheel down
pyautogui.scroll(-10)
