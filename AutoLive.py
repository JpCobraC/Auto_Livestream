import os
import psutil
import pyautogui
import pygetwindow as gw
import logging
import time
import schedule
from datetime import datetime

logging.basicConfig(
    filename='meu_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def abre_programa(nome_programa, caminho_programa):
    if any(nome_programa.lower() in p.info['name'].lower() for p in psutil.process_iter(['name'])):
        logging.info(f"Func: abre_programa | {nome_programa} já está em execução.")
    else:
        try:
            os.startfile(caminho_programa)
            logging.info(f"Func: abre_programa | {nome_programa} iniciado com sucesso.")
        except Exception as e:
            logging.error(f"Func: abre_programa | Erro ao tentar iniciar {nome_programa}: {e}")

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
                abre_programa(nome_programa)

def preparar_inicio():
    # Seleciona live já programada
    abre_janela('obs64')
    time.sleep(2)
    pyautogui.click(1270, 489)
    time.sleep(1)
    pyautogui.click(509, 61)
    time.sleep(1)

    # Coloca cópia do telão no programa 
    pyautogui.click()
    time.sleep()

def inicia_live():
    pyautogui.click()
    time.sleep(1)

def cam1_programa():
    pyautogui.click()
    time.sleep(1)

# Abrir programas necessários:
programas = {
    'obs64': r'C:/Program Files/obs-studio/bin/64bit/obs64.exe',
    'firefox': r'C:/Program Files/Mozilla Firefox/firefox.exe'
}

for nome,caminho in programas.items():
    abre_programa(nome, caminho)

# Agendamento:
schedule.every().tuesday.at("19:23").do(preparar_inicio)
schedule.every().tuesday.at("19:25").do(inicia_live)
schedule.every().tuesday.at("19:30").do(cam1_programa)

schedule.every().saturday.at("19:23").do(preparar_inicio)
schedule.every().saturday.at("19:25").do(inicia_live)
schedule.every().saturday.at("19:30").do(cam1_programa)

schedule.every().sunday.at("18:53").do(preparar_inicio)
schedule.every().sunday.at("18:55").do(inicia_live)
schedule.every().sunday.at("19:00").do(cam1_programa)

while True:
    schedule.run_pending()
    time.sleep(1)