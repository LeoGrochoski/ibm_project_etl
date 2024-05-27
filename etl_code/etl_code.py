import pandas as pd # Biblioteca para manipulação de dados em CSV e JSON e transformação em dados tabulares
import glob # Biblioteca para trabalhar com arquivos e diretorios
import xml.etree.ElementTree as ET # Biblioteca para manipulação de dados XML
from datetime import datetime # Biblioteca para trabalhar com data e horario, muito utilizada para geração de logs. 

def extracao_csv(arquivo):
    """
    Função para extrair dados dos arquivos .csv
    """
    dados_csv = pd.read_csv(arquivo)
    return dados_csv


def extracao_json(arquivo):
    """
    Função para extrair dados dos arquivos .json
    """
    dados_json = pd.read_json(arquivo, lines=True)
    return dados_json


def extracao_xml(arquivo):
    """
    Função para extrair dados dos arquivos .json
    """
    dados_xml = pd.DataFrame(columns=["nome", "email", "telefone", "endereco", "renda"])
    arvore = ET.parse(arquivo)
    raiz = arvore.getroot()

    for registro in raiz:
        nome = registro.find("nome").text
        email = registro.find("email").text
        telefone = registro.find("telefone").text
        endereco = registro.find("endereco").text
        renda = float(registro.find("renda").text)
        dados_xml = pd.concat([dados_xml, pd.DataFrame([{"nome":nome, "email":email, "telefone":telefone, "endereco":endereco, "renda":renda}])], ignore_index=True)
    return dados_xml

# A logica que utilizarei é a criação de um DF vazio para persistir os dados 
# e depois extrair os dados de cada extensáo e concatena-las no dataframe vazio.

def extracao():
    """
    Função para extração dos dados baseado em sua extensão, primeiro criaremos um dataframe para persistir os dados
    depois processaremos os arquivos respectivos por extensão e por fim retornaremos os dados extraidos.
    """
    dados_extraidos = pd.DataFrame(columns=['nome', 'email', 'telefone', 'endereco', 'renda'])
    
    # Processando os dados do arquivo csv
    for arquivo_csv in glob.glob("*.csv"):
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_csv(arquivo_csv))], ignore_index=True)
    
    # Processando os dados do arquivo json
    for arquivo_json in glob.glob("*.json"):
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_csv(arquivo_json))], ignore_index=True)
    
    # Processando os dados do arquivo xml
    for arquivo_xml in glob.glob("*.xml"):
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_csv(arquivo_xml))], ignore_index=True)

    return dados_extraidos


# Sugestão de Melhoria: Incluir type hint nas fucões