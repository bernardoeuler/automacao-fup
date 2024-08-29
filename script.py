import pyautogui
import pyperclip
import subprocess
from time import sleep
from utils.webscraping import getElement
from utils.filehandling import createPythonFile

pyautogui.PAUSE = 1

number = input("Digite o número desta tarefa: ")
quantity = int(input("Quantas questões tem essa tarefa? "))
print(f'Crie aqui uma pasta com o nome "Tarefa {number}"')
pause = 0
if input("Gostaria de configurar uma pausa para o programa esperar um site abrir? (S/N) ")[0].strip().upper() == "S":
    try:
        pause = int(input("De quantos segundos de pausa você precisa? "))
    except ValueError or TypeError:
        print("Digite somente números inteiros.")
        exit()
print('Entre na página "Teste suas questões".')
print('Clique em "Continuar sua tentativa" ou, se já tiver concluído, vá para a melhor tentativa e clique em "Revisão"')
print('Clique em "Mostrar uma página por vez".')
print("Copie a url da página.")
url = input("Cole aqui a url copiada: ")

if url.count("#"):
    i = url.rindex("#")
    url = url[:i]

print("...")
sleep(1)

pyautogui.press("win")
pyautogui.typewrite("chrome", interval=0.025)
pyautogui.press("enter")

for i in range(quantity):
    pyautogui.hotkey("alt", "d")
    pyperclip.copy(f"{url}&page={i}")
    url = pyperclip.paste()
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    if pause > 0:
        sleep(pause)
    pyautogui.hotkey("ctrl", "u")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    html = pyperclip.paste()
    code = getElement(html, "textarea", "class", "coderunner-answer")[0].text.strip()
    createPythonFile(code, f"Tarefa {number}/{i + 1}.py")
    pyautogui.hotkey("ctrl", "w")

subprocess.Popen(f'ruff format \"Tarefa {number}\"', shell=True)
exit()