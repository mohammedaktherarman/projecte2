from client import db_client

def get_influencers():
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM influencer")
    influencers = cursor.fetchall()
    conn.close()
    return influencers

def get_influencer(id):
    conn = db_client() 
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM influencer WHERE id_influencer = %s", (id,))
    influencer = cursor.fetchone()
    conn.close()
    return influencer

def create_influencer(influencer):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        INSERT INTO influencer (nom, email, password, telefon, redesSociales, descripcio, ubicacio, industria_sector)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        influencer.nombre, influencer.email, influencer.password, influencer.telefono, 
        influencer.redes_sociales, influencer.descripcion, influencer.ubicacion, influencer.industria_sector
    ))
    conn.commit()
    conn.close()

def update_influencer(id, influencer):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        UPDATE influencer
        SET nom = %s, email = %s, password = %s, telefon = %s, redesSociales = %s, descripcio = %s, ubicacio = %s, industria_sector = %s
        WHERE id_influencer = %s
    """
    cursor.execute(query, (
        influencer.nombre, influencer.email, influencer.password, influencer.telefono, 
        influencer.redes_sociales, influencer.descripcion, influencer.ubicacion, influencer.industria_sector, id
    ))
    conn.commit()
    conn.close()

def delete_influencer(id):
    conn = db_client() 
    cursor = conn.cursor()
    cursor.execute("DELETE FROM influencer WHERE id_influencer = %s", (id,))
    conn.commit()
    conn.close()

def get_empresas():
    conn = db_client() 
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empresa")
    empresas = cursor.fetchall()
    conn.close()
    return empresas

def get_empresa(id):
    conn = db_client()  
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empresa WHERE id_empresa = %s", (id,))
    empresa = cursor.fetchone()
    conn.close()
    return empresa

def create_empresa(empresa):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        INSERT INTO empresa (nom, email, telefon, password, web_empresa, descripcio, ubicacio, industria_sector)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        empresa.nombre, empresa.email, empresa.telefono, empresa.password, 
        empresa.web_empresa, empresa.descripcion, empresa.ubicacion, empresa.industria_sector
    ))
    conn.commit()
    conn.close()

def update_empresa(id, empresa):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        UPDATE empresa
        SET nom = %s, email = %s, telefon = %s, password = %s, web_empresa = %s, descripcio = %s, ubicacio = %s, industria_sector = %s
        WHERE id_empresa = %s
    """
    cursor.execute(query, (
        empresa.nombre, empresa.email, empresa.telefono, empresa.password, 
        empresa.web_empresa, empresa.descripcion, empresa.ubicacion, empresa.industria_sector, id
    ))
    conn.commit()
    conn.close()

def delete_empresa(id):
    conn = db_client() 
    cursor = conn.cursor()
    cursor.execute("DELETE FROM empresa WHERE id_empresa = %s", (id,))
    conn.commit()
    conn.close()

def get_ofertas():
    conn = db_client() 
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM oferta")
    ofertas = cursor.fetchall()
    conn.close()
    return ofertas

def get_oferta(id):
    conn = db_client() 
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM oferta WHERE id_oferta = %s", (id,))
    oferta = cursor.fetchone()
    conn.close()
    return oferta

def create_oferta(oferta):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        INSERT INTO oferta (id_empresa, id_influencer, titol, descripcio, pressupost, requisits)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        oferta.id_empresa, oferta.id_influencer, oferta.titol, oferta.descripcio,
        oferta.pressupost, oferta.requisits
    ))
    conn.commit()
    conn.close()

def update_oferta(id, oferta):
    conn = db_client() 
    cursor = conn.cursor()
    query = """
        UPDATE oferta
        SET id_empresa = %s, id_influencer = %s, titol = %s, descripcio = %s, pressupost = %s, requisits = %s
        WHERE id_oferta = %s
    """
    cursor.execute(query, (
        oferta.id_empresa, oferta.id_influencer, oferta.titol, oferta.descripcio,
        oferta.pressupost, oferta.requisits, id
    ))
    conn.commit()
    conn.close()

def delete_oferta(id):
    conn = db_client()  
    cursor = conn.cursor()
    cursor.execute("DELETE FROM oferta WHERE id_oferta = %s", (id,))
    conn.commit()
    conn.close()
