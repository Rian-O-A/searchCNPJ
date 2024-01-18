import json
with open('app\source\config.json') as arquivo:
        config = json.load(arquivo)

def pesquisar(data):
    import requests
    
    
    

    # Faz a requisição POST
    response = requests.post(config["url"]+"/search", json=data, headers=config["headers"])

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        cleanFormat = []
        response = response.json()["data"]["cnpj"]
        for data in response:
            print("------------------------------")
            print(f"razao_social :{data['razao_social']}\ncpnj: {data['cnpj']}")
            
            formatRequest = FormatUrl(data['razao_social'], (data['cnpj']))
            print(formatRequest)
            responsePlus = requests.get(config["url"]+ f"/{formatRequest}", headers=config["headers"]).json()
            # print(responsePlus)
            cleanFormat.append(responsePlus["cnpj"])
        # Converte a resposta para JSON e imprime
    
        return cleanFormat
        
        
    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        print(response.text)
        return None
    
    
def FormatUrl(razaoSocial, cnpj):
    FormatRazaoSocial = razaoSocial.split()
    if FormatRazaoSocial[-1].isdigit():
        FormatRazaoSocial = FormatRazaoSocial[:-2]
    if FormatRazaoSocial[0].isdigit():
        FormatRazaoSocial = FormatRazaoSocial[1:]
        
    FormatRazaoSocial = '-'.join(FormatRazaoSocial)
        
    
    return FormatRazaoSocial.replace("/", "").replace('.', '').lower() +'-'+cnpj
    