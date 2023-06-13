import pyautogui
import time

while True:
    try:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Move the mouse slightly to the right and then return to the original position
        pyautogui.moveTo(x + 10, y + 50)
        pyautogui.moveTo(x, y)

        # Wait 5 seconds before repeating the movement
        time.sleep(5)
    except KeyboardInterrupt:
        break