import pyautogui

pyautogui.screenshot("d:\\screenshot.png")

print(pyautogui.locateOnScreen('d:\\google.png'))

coordinate=pyautogui.locateCenterOnScreen('d:\\google.png')
print(coordinate)
pyautogui.moveTo(coordinate,duration=1)
pyautogui.click(coordinate)