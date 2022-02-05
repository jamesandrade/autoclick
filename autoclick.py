import pyautogui,time

#funcionalidades p/ implementar:

#definir dois pontos X1, Y1 e X2, Y2 para click 
#definir os pontos onde ocorrerão a captura de cor
#definir o que fazer ao detectar cada cor
#definir a cada xx tempo ocorrerá a execução do script


x = 200
y = 200

color = (12, 12, 12)

s = pyautogui.screenshot()

print(s.getpixel((x, y)))
if s.getpixel((x, y)) == color:
    pyautogui.click(x, y)
    time.sleep(0.5)
