import json
import requests
with open('app\source\config.json') as arquivo:
        config = json.load(arquivo)
        
        
class Pesquisar:
    

    def package(self, data):
        
        # Faz a requisição POST
        response = requests.post(config["url"]+"search", json=data, headers=config["headers"])

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            cleanFormat = []
            response = response.json()["data"]["cnpj"]
            for data in response:
                responsePlus = self.InfoCNPJ(data['cnpj'])
                cleanFormat.append(responsePlus["cnpj"])
            
        
            return cleanFormat
            
            
        else:
            raise ValueError(f"Algo inesperado ocorreu. Código de status: {response.status_code}")
        

    def InfoCNPJ(self, cnpj):
        
        link = config["url"]+ cnpj
        response= requests.get(link, headers=config["headers"])
        
        if response.status_code == 200:
            return response.json() 
        else:
            raise ValueError(f"Algo inesperado ocorreu na pesquisa desse cnpj. Código de status: {response.status_code}")
        
    