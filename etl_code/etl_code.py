import pandas as pd # Biblioteca para manipulação de dados em CSV e JSON e transformação em dados tabulares
import glob # Biblioteca para trabalhar com arquivos e diretorios
import xml.etree.ElementTree as ET # Biblioteca para manipulação de dados XML
from datetime import datetime # Biblioteca para trabalhar com data e horario, muito utilizada para geração de logs. 

def extracao_csv(arquivo):
    dados_csv = pd.read_csv(arquivo)
    return dados_csv


def extracao_json(arquivo):
    dados_json = pd.read_json(arquivo, lines=True)
    return dados_json


def extracao_xml(arquivo):
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