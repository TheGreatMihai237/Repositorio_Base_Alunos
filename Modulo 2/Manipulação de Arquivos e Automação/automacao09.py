import pyautogui, time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Desenhando com pyautogui")
pyautogui.press("enter")
time.sleep(2)

arvore = [
    "vvvvvvvvvvvvv",
    " ___      ___",
    "(  )     (  )",
    "     L       ",
    "    -----    ",
    "\           /",
    "     ---     "
]

for linha in arvore:
    pyautogui.write(linha, interval =0.02)
    pyautogui.press("enter")
print("Desenho de um menino")