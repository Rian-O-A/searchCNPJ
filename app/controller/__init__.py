import json
import os
from app.controller.save import saveJSON
from app.web.scraping import Pesquisar


def start(pages=None, path=None, search=None):
    
    try:
        if path:
            if not os.path.exists(path):
                
                raise ValueError(f'Caminho "{path}" não encontrado!')
            
        if search:
            response = Pesquisar.InfoCNPJ(cnpj=search)
            saveJSON(packet=response, path=path)
            
                
        
        if pages:    
            from tqdm import tqdm
            progress_bar = tqdm(total=pages, desc="Progresso")
            packetCNPJ = []
            with open(r'app\source\filters.json') as arquivo:
                data = json.load(arquivo)    
            
            
            for page in range(1, pages+1):
                data["page"] = page
            
                response = Pesquisar.package(data= data)
                packetCNPJ.extend(response)
                progress_bar.update(1)
                
            progress_bar.close()  
            saveJSON(packet=packetCNPJ, path=path)
    
    except ValueError as e:
        print(f"Error: {e}")
    