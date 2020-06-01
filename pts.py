import pyautogui
import time


time.sleep(5)  # initial delay for opening twitch stream
i = 0  # How many times button was clicked

with open('output.txt', 'a') as ouf:
    ouf.write('Initial time of the start' + ' ')  # Logging the time of the start
    ouf.write(time.asctime() + '\n')

while True:
    button_points = pyautogui.locateOnScreen('reward_button.png', confidence=0.7)

    # Looks for a picture in confidence of 80 percent

    if button_points is None:
        time.sleep(10)  # Waits 10 seconds before checking again
    else:
        button_location = pyautogui.center(button_points)  # Locates the center of a button
        pyautogui.click(button_location)  # Clicks the button
        i += 1  # Increments amount of clicks

        with open('output.txt', 'a') as ouf:  # Working with output file
            ouf.write(str(i) + ' ')  # Output in file
            ouf.write(time.asctime() + '\n')
