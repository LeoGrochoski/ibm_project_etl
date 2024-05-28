
def transformacao(dados): 
    dados['price'] = round(dados["price"], 2)
    
    return dados 