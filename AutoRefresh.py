import pyautogui,time
refr=int(input("How many times: "))
time.sleep(5)
for i in range(refr):
    pyautogui.moveTo(1193,184)
    pyautogui.rightClick()
    pyautogui.moveTo(1143,263)
    pyautogui.click()