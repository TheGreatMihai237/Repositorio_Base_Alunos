#Crie uma automação que faça o mouse se mover na forma 
# de um quadrado importamos a biblioteca pyautogui
import pyautogui

for i in range(10):
    # a função .moveTo é uma função para movimento do mouse
    # pyautogui.moveTo(x,y,duration=em segundos)
    pyautogui.moveTo(100+10 * i, 100 + 10 * i,durations=0.25)
    pyautogui.moveTo(100+10 * i, 100 + 10 * i,durations=0.25)
    pyautogui.moveTo(100+10 * i, 100 + 10 * i,durations=0.25)
    pyautogui.moveTo(100+10 * i, 100 + 10 * i,durations=0.25)