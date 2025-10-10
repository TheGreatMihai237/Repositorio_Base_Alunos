import pyautogui
import time

time.sleep(2)

# Pressiona Win + R para abrir o Executar
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Digita 'calc' e pressiona Enter para abrir a Calculadora
pyautogui.write('calc')
pyautogui.press('enter')

# Aguarda a calculadora abrir
time.sleep(2)

# Digita 8 + 2 =
pyautogui.write("8 + 2")
pyautogui.press("Enter")
time.sleep(3)