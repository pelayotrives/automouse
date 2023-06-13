import pyautogui
import time
import random

while True:
    try:
        # Get the current mouse position.
        x, y = pyautogui.position()

        # Generate random coordinates within a range
        random_x = random.randint(x - 10, x + 10)
        random_y = random.randint(y - 10, y + 10)

        # Move the mouse slightly and then return to the original position.
        pyautogui.moveTo(x + 10, y + 50)
        pyautogui.moveTo(x, y)

        # Wait 5 seconds before repeating the movement.
        time.sleep(5)
    except KeyboardInterrupt:
        break