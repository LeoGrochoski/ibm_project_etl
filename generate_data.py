import csv
import json
import xml.etree.ElementTree as ET
from faker import Faker
from unidecode import unidecode

fake = Faker('pt_BR') # Setei portugues para gerar os dados de clientes

def gerar_dados(num_registros=20):
    """
    Esta função tem o objetivo de gerar dados sintéticos para os clientes,
    estes dados são gerados a partir da biblioteca faker.
    """
    dados = []
    for _ in range(num_registros):
        dados.append({
            "nome": unidecode(fake.name()),
            "email": unidecode(fake.email()),
            "telefone": unidecode(fake.phone_number()),
            "endereco": unidecode(fake.address()),
            "renda": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return dados

def salvar_csv(dados, nome_arquivo):
    """
    Salva os dados em formato CSV.
    """
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'email', 'telefone', 'endereco', 'renda']
        gerador = csv.DictWriter(arquivo_csv, fieldnames=campos)

        gerador.writeheader()
        for dado in dados:
            gerador.writerow(dado)

def salvar_json(dados, nome_arquivo):
    """
    Salva os dados em formato JSON.
    """
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def salvar_xml(dados, nome_arquivo):
    """
    Salva os dados em formato XML.
    """
    raiz = ET.Element("dados")
    for dado_x in dados:
        registro = ET.SubElement(raiz, "registro")
        for chave, valor in dado_x.items():
            ET.SubElement(registro, chave).text = str(valor)

    tree = ET.ElementTree(raiz)
    tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)

# Criação das variaveis que receberão path para criação dos arquivos
csv_nome_arquivo = 'C:\Lab\ibm_project_etl\data\dados_clientes.csv'
json_nome_arquivo = 'C:\Lab\ibm_project_etl\data\dados_clientes.json'
xml_nome_arquivo = 'C:\Lab\ibm_project_etl\data\clientes.xml'

dados = gerar_dados() # Gerando os dados

# Chamando as funções para salvar os arquivos de dados
salvar_csv(dados, csv_nome_arquivo)
salvar_json(dados, json_nome_arquivo)
salvar_xml(dados, xml_nome_arquivo)

# Retorna os nomes dos arquivos
csv_nome_arquivo, json_nome_arquivo, xml_nome_arquivo