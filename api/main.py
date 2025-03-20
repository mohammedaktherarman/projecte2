from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from db_fluence import (
    get_influencers, get_influencer, create_influencer, update_influencer, delete_influencer,
    get_empresas, get_empresa, create_empresa, update_empresa, delete_empresa,
    get_ofertas, get_oferta, create_oferta, update_oferta, delete_oferta
)

class Influencer(BaseModel):
    id_influencer: Optional[int] = None  
    nombre: str
    email: str
    password: Optional[str] = None
    telefono: Optional[str] = None
    redes_sociales: Optional[str] = None  
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None 
    industria_sector: Optional[str] = None  

class Empresa(BaseModel):
    id_empresa: Optional[int] = None 
    nombre: str
    email: str
    password: Optional[str] = None  
    telefono: Optional[str] = None
    web_empresa: Optional[str] = None  
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None 
    industria_sector: Optional[str] = None  

class Oferta(BaseModel):
    id_oferta: Optional[int] = None 
    id_empresa: int 
    id_influencer: Optional[int] = None  
    titol: str
    descripcio: Optional[str] = None
    pressupost: Optional[float] = None
    requisits: Optional[str] = None

app = FastAPI()

@app.get("/influencers/")
def read_influencers():
    try:
        return {"status": "ok", "data": get_influencers()}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.get("/influencer/{id}")
def read_influencer(id: int):
    try:
        return {"status": "ok", "data": get_influencer(id)}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.post("/influencer/")
def add_influencer(influencer: Influencer):  
    try:
        create_influencer(influencer)
        return {"status": "ok", "missatge": "Influencer creat correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.put("/influencer/{id}")
def modify_influencer(id: int, influencer: Influencer): 
    try:
        update_influencer(id, influencer)
        return {"status": "ok", "missatge": "Influencer actualitzat correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.delete("/influencer/{id}")
def remove_influencer(id: int):
    try:
        delete_influencer(id)
        return {"status": "ok", "missatge": "Influencer eliminat correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.get("/empresas/")
def read_empresas():
    try:
        return {"status": "ok", "data": get_empresas()}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.get("/empresa/{id}")
def read_empresa(id: int):
    try:
        return {"status": "ok", "data": get_empresa(id)}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.post("/empresa/")
def add_empresa(empresa: Empresa):  
    try:
        create_empresa(empresa)
        return {"status": "ok", "missatge": "Empresa creada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.put("/empresa/{id}")
def modify_empresa(id: int, empresa: Empresa):  
    try:
        update_empresa(id, empresa)
        return {"status": "ok", "missatge": "Empresa actualitzada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.delete("/empresa/{id}")
def remove_empresa(id: int):
    try:
        delete_empresa(id)
        return {"status": "ok", "missatge": "Empresa eliminada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.get("/ofertas/")
def read_ofertas():
    try:
        return {"status": "ok", "data": get_ofertas()}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.get("/oferta/{id}")
def read_oferta(id: int):
    try:
        return {"status": "ok", "data": get_oferta(id)}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.post("/oferta/")
def add_oferta(oferta: Oferta): 
    try:
        create_oferta(oferta)
        return {"status": "ok", "missatge": "Oferta creada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.put("/oferta/{id}")
def modify_oferta(id: int, oferta: Oferta): 
    try:
        update_oferta(id, oferta)
        return {"status": "ok", "missatge": "Oferta actualitzada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}

@app.delete("/oferta/{id}")
def remove_oferta(id: int):
    try:
        delete_oferta(id)
        return {"status": "ok", "missatge": "Oferta eliminada correctament."}
    except Exception as e:
        return {"status": "error", "missatge": str(e)}
