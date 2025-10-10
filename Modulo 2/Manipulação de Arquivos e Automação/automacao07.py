# automação de login ficticio
# ideia: preencher automaticamente um formulario (html local ou simulado, via bloco de notas)

import pyautogui, time # outra maneira de escrever a importação
time.sleep(3)
pyautogui.write("aluno_python", interval=0.03)
pyautogui.press("tab")
pyautogui.write("senha123", interval=0.03)
pyautogui.press("enter")
