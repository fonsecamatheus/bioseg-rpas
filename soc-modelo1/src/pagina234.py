from time import sleep

import clipboard
import pyautogui


def pagina234(pagina, dict_empresas):
    for cod_empresa, nome_empresa in dict_empresas.items():
        
        # Clicando no botão p/ trocar de empresa
        btn_trocar_empresa = pagina.locator('#barraIcones > ul > li:nth-child(2) > a')
        btn_trocar_empresa.click()
        sleep(1)

        # Setando cod_empresa em pesquisar
        pyautogui.moveTo(808, 508)
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.write(cod_empresa)
        sleep(1)

        # Clicando na lupa de pesquisa
        pyautogui.moveTo(1010, 508)
        sleep(1)
        pyautogui.click()
        sleep(1)

        # Clicando no nome da empresa
        pyautogui.moveTo(808, 540)
        sleep(1)
        pyautogui.click()
        sleep(1)

        # Navegando para a página 234
        pagina.fill('//*[@id="cod_programa"]', '234')
        sleep(1)
        pagina.locator('//*[@id="btn_programa"]').click()
        sleep(3)

        # Clicando no botão p/ gerar o pedido de processamento
        pagina.keyboard.press('Tab')
        sleep(1)
        pagina.keyboard.press('Tab')
        sleep(1)
        pagina.keyboard.press('Enter')
        sleep(1)

        # Copiando e colando n° do pedido de processamento
        pagina.keyboard.press('Control+A')
        sleep(1)
        pagina.keyboard.press('Control+C')
        sleep(1)
        copia_pagina = clipboard.paste()
        sleep(1)
        numero_pedido = copia_pagina[-28:-19]
        sleep(1)

        # Adicionando o n° do pedido de processamento no dicionário dict_empresas
        if cod_empresa in dict_empresas:
            if isinstance(dict_empresas[cod_empresa], list):
                dict_empresas[cod_empresa].append(numero_pedido)
            else:
                dict_empresas[cod_empresa] = [dict_empresas[cod_empresa], numero_pedido]
        else:
            dict_empresas[cod_empresa] = [numero_pedido]

    # Verificando se o n° do pedido de processamento é composto apenas por números
    codigos_para_remover = []
    for chave, valor in dict_empresas.items():
        print('EMPRESA: ',valor[0], '--->', 'PEDIDO DE PROCESSAMENTO: ',valor[1])
        if not valor[1].isdigit():
            codigos_para_remover.append(chave)
    
    # Removendo o códigos das empresas que possuem letras no n° de pedido de processamento
    for chave in codigos_para_remover:
        print(f'EMPRESA {valor[0]} DEVERÁ REALIZAR O DOWNLOAD MANUALMENTE DA MODELO 1')
        del dict_empresas[chave]

    return dict_empresas
