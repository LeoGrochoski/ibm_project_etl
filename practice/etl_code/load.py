from datetime import datetime 
import pandas as pd
from transform import transformacao
from extract import extracao

arquivo_log = "arquivo_log.txt" 
arquivo_salvo = "dados_prontos.csv" 

def carrega_dados(arquivo_salvo, dados_transformados): 
    dados_transformados.to_csv(arquivo_salvo)
    
def progresso_log(mensagem): 
    formato_timestamp = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(formato_timestamp) 
    with open(arquivo_log,"a") as f: 
        f.write(mensagem + "[" + timestamp + "]"'\n') 
        
# Log da inicialização do processo de ETL
progresso_log("ETL Iniciado: ") 
 
# Log do inicio da etapa de extracao 
progresso_log("Fase de Extracao iniciada: ") 
dados_extraidos = extracao() 
 
# Log do processo de extracao completo 
progresso_log("Fase de Extracao finalizada: ") 
 
# Log do inicio da etapa de transformacao 
progresso_log("Fase de Transformacao iniciada: ") 
dados_transformados = transformacao(dados_extraidos) 
print("Dados Transformados: ") 
print(dados_transformados) 
 
# Log do processo de transformacao completo 
progresso_log("Fase de Transformacao finalizada: ") 
 
# Log do inicio da etapa de carregamento 
progresso_log("Fase de Carregamento iniciada: ") 
carrega_dados(arquivo_salvo,dados_transformados) 
 
# Log do processo de carregamento completo 
progresso_log("Fase de Carregamento finalizado: ") 
 
# Log do ETL completo
progresso_log("ETL Finalizado: ")