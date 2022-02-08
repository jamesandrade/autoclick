import pyautogui,time

x = 1032
y = 620

x2 = 1302
y2 = 505

x3 = 1200
y3 = 370

x4 = 1290
y4 = 370

x5 = 1290
y5 = 396

colorDown = (220, 20, 60) #down
colorUp =(0, 128, 0) #up
colorOff = (33, 33, 33)

up = False
down = False

while True:
    s = pyautogui.screenshot()
    #print(s.getpixel((x2, y2)))
    if s.getpixel((x2, y2)) == colorOff:
        up = False
        down = False
       
    if s.getpixel((x2, y2)) != colorOff and (s.getpixel((x, y)) == colorUp or s.getpixel((x, y)) == colorDown):
        if  s.getpixel((x, y)) == colorUp and up == True:
            time.sleep(60)            
        elif  s.getpixel((x, y)) == colorUp and down == True:    
            pyautogui.click(x5, y5)
            up = True
            down = False
            time.sleep(60)
        elif  s.getpixel((x, y)) == colorDown and down == True:
            time.sleep(60)                
        elif  s.getpixel((x, y)) == colorDown and up == True:    
            pyautogui.click(x5, y5)
            down = True
            up = False
            time.sleep(60)
            
    elif s.getpixel((x, y)) == colorDown:
         pyautogui.click(x4, y4)
         down = True
         time.sleep(60)

         
    elif s.getpixel((x, y)) == colorUp:
        pyautogui.click(x3, y3)
        up = True
        time.sleep(60)
    