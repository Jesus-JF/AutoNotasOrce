import subprocess
import pyautogui
import time

################################################# Vscode

command = '"D:\\Microsoft VS Code\\Code.exe"'
subprocess.Popen(command) 
time.sleep(3)
pyautogui.hotkey('altleft','space')
pyautogui.hotkey('x')
pyautogui.FAILSAFE = True
################################################# Github
time.sleep(2)
#command = '"D:\\Vivaldi\\Application\\vivaldi.exe"'  # es necesario la dos barras diagonales sino se malogra la interpretacion.
#subprocess.Popen(command)

# Si en vez de utilizar Vivaldi utilizas Chrome comenta las dos lineas anteriores y descomenta las 5 que siguen
pyautogui.hotkey('winleft')
time.sleep(1)
pyautogui.typewrite('chrome')
time.sleep(1)
pyautogui.hotkey('enter')

time.sleep(3) #que espere a que se cargue la aplicacion.
pyautogui.hotkey('altleft','space') #por si la ventana IMPREDESDCIBLEMENTE se abre en modo pequeña ventana y no pantalla completa. Por suerte conozco los atajos de teclado
#pyautogui.keyDown('x')
#pyautogui.keyup('x')
pyautogui.hotkey('x') #con este si sale
pyautogui.FAILSAFE = True #si el puntero pierde el control, pondriamos el cursor en rincon izquierdo arriba y pierde el control python ,lo retomamos nosotros.

pyautogui.moveTo(664,629,duration=1)
pyautogui.click(664,629,button='left')

time.sleep(2)
pyautogui.hotkey('ctrlleft','t',)
time.sleep(2)
pyautogui.hotkey('ctrlleft','l',)
time.sleep(1)
pyautogui.typewrite('https://github.com')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
################################################# StackOverflow
pyautogui.hotkey('ctrlleft','t',)
time.sleep(2)
pyautogui.hotkey('ctrlleft','l',)
time.sleep(1)
pyautogui.typewrite('https://stackoverflow.com')
time.sleep(3)
pyautogui.press('enter')
time.sleep(5)

################################################# Spotify
time.sleep(1)
pyautogui.hotkey('winleft')
time.sleep(1)
pyautogui.typewrite('spotify')
time.sleep(1)
pyautogui.hotkey('enter')
################################################# CLOSE APPLICATIONS

subprocess.call(["taskkill","/F","/IM","vivaldi.exe"])
subprocess.call(["taskkill","/F","/IM","zoom.exe"])
# subprocess.call(["taskkill","/F","/IM","spotify.exe"])
subprocess.call(["taskkill","/F","/IM","chrome.exe"])

