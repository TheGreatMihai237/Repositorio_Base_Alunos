1 # passo 1: instalar o py autogui com o comando:
# pip install pyautogui

#Crie uma automação, que abra automaticamente o navegador


# importamos a biblioteca para o script em uso
import pyautogui

# "press" é um comando que utilizamos para pressionar a 
#tecla desejada
pyautogui.press("Win")# para pressionar a tleca windows

#"sleep" é um comando que utilizamos para deixar o código 0
#em espera por alguns segundos

pyautogui.sleep(1)

#write é um comando para passar o que queremos escrever
pyautogui.write("google chrome")

pyautogui.press("Enter")