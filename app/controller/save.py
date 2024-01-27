import json
import uuid
import sys

def saveJSON(packet, path):
    nameFile = uuid.uuid4()
    
    path = f"{path}/{nameFile}.json" if path else f"{sys.path[0]}\{nameFile}.json"
    
    json.dump(packet, open(path, 'w', encoding=("UTF-8")), indent=6, ensure_ascii=False)
    print("======================= SAVED PACKAGE ========================")
    print(f"Path: {path}")
    print(f"Itens encontrados: {len(packet)}")
    print("==============================================================")
    
    
    
    