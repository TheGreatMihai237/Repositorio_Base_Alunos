import pyautogui
import webbrowser
import time

# Passo 1> abri o youtube com uma música especifica 
url = "https://www.youtube.com/watch?v=oX-xhOB5MF4"
webbrowser.open(url)

# aguardar o carregamento da pagina
time.sleep(5) # ajustar de acordo com a velocidade da sua internet

# passo 3: garantir que o video comece ( aperte espaço para play)
pyautogui.press("space")
# começar o video
