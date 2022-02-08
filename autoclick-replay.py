import pyautogui,time

x = 1032
y = 620

x2 = 1302
y2 = 505

x3 = 1200
y3 = 370

x4 = 1290
y4 = 370

colorDown = (220, 20, 60) #down
colorUp =(0, 128, 0) #up
colorC = (98, 78, 25)
colorC2 = (98, 78, 25)
colorV = (29, 80, 49)

while True:
    s = pyautogui.screenshot()
    print(s.getpixel((x2, y2)))
    if s.getpixel((x2, y2)) == colorC or s.getpixel((x2, y2)) == colorV or s.getpixel((x2, y2)) == colorC2:
        time.sleep(0.5)
    elif s.getpixel((x, y)) == colorDown:
         pyautogui.click(x4, y4)
         time.sleep(60)
    elif s.getpixel((x, y)) == colorUp:
        pyautogui.click(x3, y3)
        time.sleep(60)
    
