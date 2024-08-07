import os
import shutil
from time import sleep
from zipfile import ZipFile

import clipboard
import pyautogui

from utils.envs import DEST


def pagina271(pagina, dict_empresas):
    dest_modelo1 = DEST
    
    # Setando a tela 271 e apertando em OK
    pagina.fill('//*[@id="cod_programa"]', '271')
    sleep(1)
    pagina.locator('//*[@id="btn_programa"]').click()
    sleep(3)
    
    # Setando o n° de pedido de processamento em pesquisar
    for i in dict_empresas.values():
        nome_empresa = i[0]
        numero_pedido = i[1]
        
        pyautogui.moveTo(500, 400)
        sleep(1)
        pyautogui.doubleClick()
        sleep(1)
        pyautogui.write('')
        sleep(1)
        pyautogui.write(numero_pedido)
        sleep(1)
        pyautogui.press('Enter')
        sleep(1)
        
        with pagina.expect_download(timeout=0) as download_info:
            copia_pagina = ''
            while 'Download' not in copia_pagina:
                sleep(1)
                pagina.keyboard.press('Enter')
                sleep(1)
                pagina.keyboard.press('Control+A')
                sleep(1)
                pagina.keyboard.press('Control+C')
                sleep(1)
                copia_pagina = clipboard.paste()
                sleep(1)

            # Clicando no botão de download
            pyautogui.moveTo(1380,535)
            sleep(2)
            pyautogui.click()
        
        # Salvando o download realizado
        download = download_info.value
        arquivo_zip = os.path.join(dest_modelo1, f'{nome_empresa}.zip')
        download.save_as(arquivo_zip)
        sleep(1)
        
        # Extraindo o arquivo xlsx da pasta zipada
        with ZipFile(arquivo_zip, 'r') as zip_ref:
            nome_novo = os.path.join(dest_modelo1, f'{nome_empresa}.xlsx')
            for arquivo in zip_ref.infolist():
                nome_arquivo = arquivo.filename
                zip_ref.extractall(path=dest_modelo1)
                shutil.move(os.path.join(dest_modelo1, nome_arquivo), nome_novo)
        os.remove(arquivo_zip)
        
            



