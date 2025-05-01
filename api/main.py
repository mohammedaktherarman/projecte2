from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from db import (
    get_influencers, get_influencer, create_influencer, update_influencer, delete_influencer,
    get_empresas, get_empresa, create_empresa, update_empresa, delete_empresa,
    verify_user
)

class Influencer(BaseModel):
    id_influencer: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    email_contacto: Optional[str] = None
    telefono: Optional[str] = None
    redsocial: Optional[str] = None
    ubicacion: Optional[str] = None
    sector: Optional[str] = None
    seguidores: Optional[str] = None
    imagen: Optional[str] = None 

class Empresa(BaseModel):
    id_empresa: Optional[int] = None
    email: str
    password: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    email_contacto: Optional[str] = None
    web: Optional[str] = None
    ubicacion: Optional[str] = None
    sector: Optional[str] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        return {"status": "ok", "message": "Influencer creado correctamente."}
    except Exception as e:
        if 'Duplicate entry' in str(e):
            raise HTTPException(status_code=400, detail="El email ya está registrado")
        return {"status": "error", "message": str(e)}

@app.put("/influencer/{id}")
def modify_influencer(id: int, influencer: Influencer):
    try:
        update_influencer(id, influencer)
        return {"status": "ok", "message": "Influencer actualizado correctamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/influencer/{id}")
def remove_influencer(id: int):
    try:
        delete_influencer(id)
        return {"status": "ok", "message": "Influencer eliminado correctamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

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
        return {"status": "ok", "message": "Empresa creada correctamente."}
    except Exception as e:
        if 'Duplicate entry' in str(e):
            raise HTTPException(status_code=400, detail="El email ya está registrado")
        return {"status": "error", "message": str(e)}

@app.put("/empresa/{id}")
def modify_empresa(id: int, empresa: Empresa):
    try:
        update_empresa(id, empresa)
        return {"status": "ok", "message": "Empresa actualizada correctamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/empresa/{id}")
def remove_empresa(id: int):
    try:
        delete_empresa(id)
        return {"status": "ok", "message": "Empresa eliminada correctamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/empresa/login")
def empresa_login(data: Empresa):
    user = verify_user("Empresa", data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"status": "ok", "message": "Inicio de sesión exitoso", "user": user}

@app.post("/influencer/login")
def influencer_login(data: Influencer):
    user = verify_user("Influencer", data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"status": "ok", "message": "Inicio de sesión exitoso", "user": user}
