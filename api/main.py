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
    apellido: str
    email: str
    password: Optional[str] = None
    telefono: Optional[str] = None
    redes_sociales: Optional[str] = None  
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None 
    categoria: Optional[str] = None  

class Empresa(BaseModel):
    id_empresa: Optional[int] = None 
    nombre: str
    email: str
    password: Optional[str] = None  
    telefono: Optional[str] = None
    web_empresa: Optional[str] = None  
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None 
    sector: Optional[str] = None  

class Oferta(BaseModel):
    id_oferta: Optional[int] = None 
    id_empresa: int 
    id_influencer: Optional[int] = None  
    titol: str
    descripcio: Optional[str] = None
    pressupost: Optional[float] = None
    requisits: Optional[str] = None
    data_inici: Optional[str] = None 
    data_finalitzacio: Optional[str] = None  
app = FastAPI()

@app.get("/influencers/")
def read_influencers():
    return get_influencers()

@app.get("/influencer/{id}")
def read_influencer(id: int):
    return get_influencer(id)

@app.post("/influencer/")
def add_influencer(influencer: Influencer):  
    return create_influencer(influencer)

@app.put("/influencer/{id}")
def modify_influencer(id: int, influencer: Influencer): 
    return update_influencer(id, influencer)

@app.delete("/influencer/{id}")
def remove_influencer(id: int):
    return delete_influencer(id)

@app.get("/empresas/")
def read_empresas():
    return get_empresas()

@app.get("/empresa/{id}")
def read_empresa(id: int):
    return get_empresa(id)

@app.post("/empresa/")
def add_empresa(empresa: Empresa):  
    return create_empresa(empresa)

@app.put("/empresa/{id}")
def modify_empresa(id: int, empresa: Empresa):  
    return update_empresa(id, empresa)

@app.delete("/empresa/{id}")
def remove_empresa(id: int):
    return delete_empresa(id)

@app.get("/ofertas/")
def read_ofertas():
    return get_ofertas()

@app.get("/oferta/{id}")
def read_oferta(id: int):
    return get_oferta(id)

@app.post("/oferta/")
def add_oferta(oferta: Oferta): 
    return create_oferta(oferta)

@app.put("/oferta/{id}")
def modify_oferta(id: int, oferta: Oferta): 
    return update_oferta(id, oferta)

@app.delete("/oferta/{id}")
def remove_oferta(id: int):
    return delete_oferta(id)
