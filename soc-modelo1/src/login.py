from time import sleep

from utils.envs import BOTAO1, BOTAO2, BOTAO3, BOTAO4, SOC_SENHA, SOC_USUARIO


def login(pagina):
    '''
    Acessando o sistema soc e setando os dados de login
    '''
    pagina.goto('https://sistema.soc.com.br/WebSoc/MainAction.do')
    sleep(1)
    pagina.locator('//*[@id="btn_ok"]').click()
    sleep(1)
    pagina.fill('//*[@id="usu"]',f'{SOC_USUARIO}')
    sleep(1)
    pagina.fill('//*[@id="senha"]',f'{SOC_SENHA}')
    sleep(1)
    pagina.get_by_role("button",name=f'{BOTAO1}').click()
    pagina.get_by_role("button",name=f'{BOTAO2}').click()
    pagina.get_by_role("button",name=f'{BOTAO3}').click()
    pagina.get_by_role("button",name=f'{BOTAO4}').click()
    sleep(1)
    pagina.locator('//*[@id="bt_entrar"]').click()
    sleep(3)
    return pagina
    




