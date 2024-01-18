import json
with open('app\source\config.json') as arquivo:
        config = json.load(arquivo)

def pesquisar(data):
    import requests
    
    
    

    # Faz a requisição POST
    response = requests.post(config["url"]+"search", json=data, headers=config["headers"])

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        cleanFormat = []
        response = response.json()["data"]["cnpj"]
        for data in response:
            responsePlus = requests.get(FormatUrl(data['cnpj']), headers=config["headers"]).json()
            cleanFormat.append(responsePlus["cnpj"])
        
    
        return cleanFormat
        
        
    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        print(response.text)
        return None
    
    
def FormatUrl(cnpj):
    
    return config["url"]+ cnpj
    