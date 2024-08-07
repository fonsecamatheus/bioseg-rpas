from time import sleep


def pulando_avisos(pagina):
    '''
    Pulando as notificações de atualização e mudança
    '''
    try:
        pagina.locator('//*[@id="naoMostrarAvisoAdministrador"]').click()
        sleep(1)
        pagina.locator('//*[@id="botaoOk"]').click()
        sleep(1)
    except Exception:
        pass
    sleep(3)
    return pagina