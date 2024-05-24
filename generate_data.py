import csv
import json
import xml.etree.ElementTree as ET
from faker import Faker
from unidecode import unidecode


fake = Faker('pt_BR')
# Função para gerar dados aleatórios usando a lib Faker
def gerar_dados(num_registros=20):
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

dados = gerar_dados()

# Criação das variaveis que receberão path para criação dos arquivos
csv_nome_arquivo = 'C:\Lab\ibm_project_etl\data\dados_clientes.csv'
json_nome_arquivo = 'C:\Lab\ibm_project_etl\data\dados_clientes.json'
xml_nome_arquivo = 'C:\Lab\ibm_project_etl\data\clientes.xml'

# Salvamento em CSV
with open(csv_nome_arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'email', 'telefone', 'endereco', 'renda']
    gerador = csv.DictWriter(arquivo_csv, fieldnames=campos)

    gerador.writeheader()
    for dado in dados:
        gerador.writerow(dado)

# Salvamento em JSON
with open(json_nome_arquivo, 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)

# Salvamento em XML
raiz = ET.Element("dados")

for dado_x in dados:
    registro = ET.SubElement(raiz, "registro")
    for chave, valor in dado_x.items():
        ET.SubElement(registro, chave).text = str(valor)

tree = ET.ElementTree(raiz)
tree.write(xml_nome_arquivo, encoding="utf-8", xml_declaration=True)

csv_nome_arquivo, json_nome_arquivo, xml_nome_arquivo

# Lembrar de tentar melhorar o codigo incluindo os saves dentro de uma função