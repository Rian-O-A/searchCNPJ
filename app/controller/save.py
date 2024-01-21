import json
import uuid
import os

def saveJSON(packet, path):
    nameFile = uuid.uuid4()
    path = f"{path}/{nameFile}.json" if path else f"{nameFile}.json"

    json.dump(packet, open(path, 'w', encoding=("UTF-8")), indent=6, ensure_ascii=False)
    print("======================= SAVED PACKAGE ========================")
    print(f"Path: {path}")
    print(f"Empresas Encontradas: {len(packet)}")
    print("==============================================================")
    