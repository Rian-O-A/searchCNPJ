import json
import uuid

def saveJSON(packet):
    path = f"app/data/{uuid.uuid4()}.json"

    json.dump(packet, open(path, 'w', encoding=("UTF-8")), indent=6, ensure_ascii=False)
    print("======================= SAVED PACKAGE ========================")
    print(f"Path: {path}")
    print(f"Empresas: {len(packet)}")
    print("==============================================================")
    