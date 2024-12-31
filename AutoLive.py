import os
import psutil
import pyautogui
import pygetwindow as gw
import logging
from datetime import datetime

logging.basicConfig(
    filename='meu_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def abre_programa(nome_programa, caminho_programa):
    if any(nome_programa.lower() in p.info['name'].lower() for p in psutil.process_iter(['name'])):
        logging.info(f"{nome_programa} já está em execução.")
    else:
        try:
            os.startfile(caminho_programa)
            logging.info(f"Func: abre_programa | {nome_programa} iniciado com sucesso.")
            return True
        except Exception as e:
            logging.error(f"Func: abre_programa | Erro ao tentar iniciar {nome_programa}: {e}")
            return False


def abre_janela(nome_programa):
    for p in psutil.process_iter(['name']):
        if nome_programa.lower() in p.info['name'].lower():
            janelas = gw.getWindowsWithTitle(nome_programa)
            if janelas:
                janela = janelas[0]
                if janela.isMinimized:
                    janela.restore()
                janela.activate()
                janela.maximize()
                logging.info(f"Func: abre_janela | Janela de {nome_programa} aberta e ativada.")
            else:
                logging.error(f"Func: abre_janela | Janela de {nome_programa} não encontrada.")
    logging.warning(f"{nome_programa} não está em execução.")
    return False

