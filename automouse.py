import pyautogui
import time
import random

while True:
    try:
        # Get the current mouse position.
        x, y = pyautogui.position()

        # Generate random coordinates within a range.
        random_x = random.randint(x - 10, x + 10)
        random_y = random.randint(y - 10, y + 10)

        # Move the mouse to new random position.
        pyautogui.moveTo(random_x, random_y)

        # Wait 5 seconds before repeating the movement.
        time.sleep(5)
    except KeyboardInterrupt:
        break