import pyautogui
import time
import math

# Circle settings
radius = 300  # Optimal radius for accuracy, change it according to your screen's resolution

# Get the screen center
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

# Function to calculate a point on the circle for a given angle
def calculate_point(angle):
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    return (x, y)

# Using only 3 points for minimal deviation
touch_points = [
    calculate_point(0),    # Right (0°)
    calculate_point(120),  # Bottom-left (120°)
    calculate_point(240),  # Top-left (240°)
]

# Countdown to switch to the game
print("Switch to the game! Starting in 3 seconds...")
time.sleep(3)

# Start drawing
pyautogui.moveTo(*touch_points[0])
pyautogui.mouseDown()

# Touch the 3 key points with minimal movement
for x, y in touch_points:
    pyautogui.moveTo(x, y, duration=0.002)  # Super fast transition

# Close the loop by returning to the first touch point
pyautogui.moveTo(*touch_points[0], duration=0.002)
pyautogui.mouseUp()

print("Perfect circle!")
