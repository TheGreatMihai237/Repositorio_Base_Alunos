# Crie uma automação que escreva um texto automaticamente

import pyautogui
import time

# aguarde 5 segundos para voce abrir o bloco de notas
time.sleep(5)

#escreva o texto
pyautogui.write("Automatizando Com pyautogui", interval=0.1)