import json
import uuid

class Filter:
    
    def getPacket(name):
        json.load(f"app\web\scraping\packetFilters\{name}.json")
    
    
    def getPackets():
        pass
    def setPacket(packet):
        json.dump(packet, open(f"app\web\scraping\packetFilters\{uuid.uuid3}.json", 'w', encoding=("UTF-8")), indent=6, ensure_ascii=False)
    
    