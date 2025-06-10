import ctypes
import os
import time
from editor import imageEditor

caminhoImagem = os.path.abspath("wallpaper.jpg")

while True:
    if os.path.isfile(caminhoImagem):
        imageEditor()
        resultado = ctypes.windll.user32.SystemParametersInfoW(20, 0, caminhoImagem, 3)
        if resultado:
            print("Papel de parede alterado com sucesso!")
        else:
            print("Falha ao alterar o papel de parede.")
    else:
        print(f"Arquivo não encontrado: {caminhoImagem}")
    time.sleep(600)
