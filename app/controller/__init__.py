import json
from app.controller.save import saveJSON
from app.web.scraping import pesquisar

def start(pages):
    from tqdm import tqdm
    progress_bar = tqdm(total=pages, desc="Progresso")
    packetCNPJ = []
    with open(r'app\source\filters.json') as arquivo:
        data = json.load(arquivo)    
    
    
    for page in range(1, pages+1):
        data["page"] = page
    
        response = pesquisar(data= data)
        packetCNPJ.extend(response)
        progress_bar.update(1)
        
    progress_bar.close()  
    saveJSON(packet=packetCNPJ)
    