#main.py
from fastapi import FastAPI , Request
import requests
import json
import  os
from typing import Annotated
from datetime import datetime

app = FastAPI()

folder_name = "bpo_payloads"
#1 comprobar si no existe la carpeta , crearla
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("ejemplo1.txt", "w") as archivo:
    archivo.write("Este es un archivo de texto creado con Python.")

estatus = "Recibido"

@app.post("/test/bpo")
async def get_json_raw(request: Request):
    # 1. Leer el stream de bytes
    raw_body = await request.body()
    # 2. Parsear manualmente
    try:
        data      = json.loads(raw_body)
        fecha_str = datetime.now().strftime("%Y%m%d%H%M%S")
        archivo   = folder_name+"/"+fecha_str+".json"

        #with open("bpo_payloads/ejemplo12.json", "w", encoding="utf-8") as f:
        with open(archivo, "w", encoding="utf-8") as f:
             json.dump(data, f, indent=4, ensure_ascii=False)
        return {"Solicitud recibida y completada": fecha_str}
    except Exception:
        return {"error": "Formato inválido"}, 400
     
    
                       
if __name__ == "__main__":
   import uvicorn
   port= int(os.getenv("PORT",8000))
   uvicorn.run(app, host="0.0.0.0", port=port)
