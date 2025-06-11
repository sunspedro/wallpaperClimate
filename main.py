# main.py
import ctypes
import os
import threading
import time
import logging
import subprocess
from editor import imageEditor, iconEditor
from pystray import Icon, Menu, MenuItem

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("appLog.log"),
        logging.StreamHandler()
    ]
)

iconEditor()
caminhoImagem = os.path.abspath("wallpaper.jpg")

def on_exit(icon, item):
    logging.info("Encerrando o aplicativo.")
    icon.stop()

def abrir_configuracoes(icon, item):
    logging.info("Abrindo configurações.")
    subprocess.Popen(["python", os.path.abspath("app.py")], shell=True)

def read_delay(default=60.0):
    try:
        with open("delay.cfg", "r") as f:
            valor = float(f.read().strip())
            logging.info(f"Delay lido de delay.cfg: {valor} segundos.")
            return valor
    except Exception as e:
        logging.debug(f"Não foi possível ler delay.cfg ({e}); usando {default}s.")
        return default

def background_task():
    while True:
        if os.path.isfile(caminhoImagem):
            logging.info("Imagem encontrada. Iniciando edição...")
            imageEditor()
            resultado = ctypes.windll.user32.SystemParametersInfoW(20, 0, caminhoImagem, 3)
            if resultado:
                logging.info("Papel de parede alterado com sucesso!")
            else:
                logging.error("Falha ao alterar o papel de parede.")
        else:
            logging.warning(f"Arquivo não encontrado: {caminhoImagem}")

        intervalo = read_delay()
        logging.info(f"Aguardando {intervalo} segundos até a próxima verificação.")
        time.sleep(intervalo)

def main():
    logging.info("Aplicativo iniciado.")
    icon = Icon(
        "WallpaperApp",
        iconEditor(),
        "Wallpaper Manager",
        menu=Menu(
            MenuItem('Abrir Configurações', abrir_configuracoes),
            MenuItem('Sair', on_exit)
        )
    )

    threading.Thread(target=background_task, daemon=True).start()
    icon.run()

if __name__ == '__main__':
    main()
