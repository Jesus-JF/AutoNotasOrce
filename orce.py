import subprocess
import pyautogui
import time

command = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'  # es necesario la dos barras diagonales sino se malogra la interpretacion.
subprocess.Popen(command)
time.sleep(2) #que espere a que se cargue la aplicacion.

# pyautogui.moveTo(669,553,duration=1)
# pyautogui.click(669,553,button='left')
# time.sleep(1)
# pyautogui.moveTo(846,437,duration=1)
# pyautogui.click(846,437,button='left')
# pyautogui.hotkey('alt','space','x')

time.sleep(1)
pyautogui.hotkey('ctrlleft','l') #por si la ventana IMPREDESDCIBLEMENTE se abre en modo pequeña ventana y no pantalla completa. Por suerte conozco los atajos de teclado
pyautogui.FAILSAFE = True
time.sleep(1)
pyautogui.typewrite('https://www.academico.uni.edu.pe/alumno/mis-notas')
time.sleep(1)
pyautogui.press("delete")
pyautogui.press("enter")

time.sleep(2)

pyautogui.moveTo(866,304,duration=0.5)
pyautogui.click(866,304,button='left')
time.sleep(0.25)
pyautogui.click(866,304,button='left')

#modificar esta linea con su codigo UNI
pyautogui.typewrite("codigouni")

pyautogui.moveTo(863,359,duration=0.5)
pyautogui.click(863,359,button='left')
time.sleep(0.25)
pyautogui.click(863,359,button='left')

#modificar esta linea con su contraseña ORCE
pyautogui.typewrite("contraseña")

pyautogui.press("enter")