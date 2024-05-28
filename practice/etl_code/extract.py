import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
import os 


dados = r"C:\Users\01701432\lab\code\practice\data_source"

def extracao_csv(arquivo): 
    dataframe = pd.read_csv(arquivo) 
    return dataframe 

def extracao_json(arquivo): 
    dataframe = pd.read_json(arquivo, lines=True) 
    return dataframe 

def extracao_xml(arquivo): 
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"]) 
    tree = ET.parse(arquivo) 
    root = tree.getroot() 
    for car in root: 
        car_model = car.find("car_model").text 
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text) 
        fuel = car.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame([{"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}])], ignore_index=True) 
    return dataframe 

def extracao(): 
    dados_extraidos = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"]) 
     
    for csvfile in glob.glob(os.path.join(dados, "*.csv")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_csv(csvfile))], ignore_index=True) 
         
    for jsonfile in glob.glob(os.path.join(dados, "*.json")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_json(jsonfile))], ignore_index=True) 
     
    for xmlfile in glob.glob(os.path.join(dados, "*.xml")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_xml(xmlfile))], ignore_index=True) 
         
    return dados_extraidos 