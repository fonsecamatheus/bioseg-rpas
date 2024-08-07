from playwright.sync_api import sync_playwright

from src.login import login
from src.pagina234 import pagina234
from src.pagina271 import pagina271
from src.pulando_avisos import pulando_avisos
from src.requisitando_empresas import (requisitando_empresas,
                                       tratamento_duplicadas)


def main(playwright):
    dados_empresas = requisitando_empresas()
    dict_empresas = tratamento_duplicadas(dados_empresas)
    
    navegador = playwright.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    
    login(pagina)
    pulando_avisos(pagina)
    dict_empresas = pagina234(pagina, dict_empresas)
    pagina271(pagina, dict_empresas)


with sync_playwright() as playwright:
    main(playwright)