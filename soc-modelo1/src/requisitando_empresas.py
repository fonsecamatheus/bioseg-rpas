import requests

from utils.envs import KEY_SOC_EMPRESAS


def requisitando_empresas():
    '''
    Requisitando os dados de empresas que possuem consultoria e e-social
    '''
    url_empresas = f'https://ws1.soc.com.br/WebSoc/exportadados?parametro={{"empresa":"887992","codigo":"151534","chave":"{KEY_SOC_EMPRESAS}","tipoSaida":"json","codigoEmpresa":"","codigoUnidade":"","dataInicio":"","dataFim":"","codigoGrupoProduto":"","estadoUnidade":"","codigoSubGrupo":"","diasAVencer":"60","codigoProduto":"2","statusEmpresa":"1","statusUnidade":"1"}}'
    rq = requests.get(url_empresas)
    dados_empresas = rq.json()
    return dados_empresas

def tratamento_duplicadas(dados_empresas):
    '''
    Tratamento realizado para remover todos os códigos de empresas duplicados
    '''
    lista_cod_empresas = {}
    for empresa in dados_empresas:
        cod_empresa = empresa.get('codigoEmpresa')
        nome_empresa = empresa.get('nomeEmpresa')
        if nome_empresa == 'DILCEU ROSSATO - 101.440.0170/80':
            nome_empresa = 'DILCEU ROSSATO - 101.440.0170-80'
        elif nome_empresa == 'SAFRAS AGROINDUSTRIA S/A':
            nome_empresa = 'SAFRAS AGROINDUSTRIA SA'
        if cod_empresa not in lista_cod_empresas:
            lista_cod_empresas[cod_empresa] = nome_empresa
    return lista_cod_empresas




