import pyautogui
import time

# Mostrando as coordenadas da tela para o Python saber onde quero clicar
# Comando: pyautogui.posision()
# Usando print para exibir o resultado desse comando

# Adicionando tempo para que seja possível mudar de tela para posicionar o mouse no campo de email e ver as coordenadas
time.sleep(5)

# Exibindo as coordenadas 
print(pyautogui.position())

# E então coloco as coordenadas em pyautogui.click()


