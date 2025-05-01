from client import db_client

def get_influencers():
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Influencer")
    influencers = cursor.fetchall()
    conn.close()
    return influencers

def get_influencer(id):
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Influencer WHERE id_influencer = %s", (id,))
    influencer = cursor.fetchone()
    conn.close()
    return influencer

def create_influencer(influencer):
    conn = db_client()
    cursor = conn.cursor()
    query = """
        INSERT INTO Influencer (email, password)
        VALUES (%s, %s)
    """
    cursor.execute(query, (influencer.email, influencer.password))
    conn.commit()
    conn.close()

def update_influencer(id, influencer):
    conn = db_client()
    cursor = conn.cursor()
    query = """
        UPDATE Influencer
        SET nom = %s, descripcio = %s, email_contacto = %s, telefon = %s,
            redsocial = %s, ubicacio = %s, sector = %s, seguidores = %s, imagen = %s
        WHERE id_influencer = %s
    """
    cursor.execute(query, (
        influencer.nombre, influencer.descripcion, influencer.email_contacto,
        influencer.telefono, influencer.redsocial, influencer.ubicacion,
        influencer.sector, influencer.seguidores, influencer.imagen, id
    ))
    conn.commit()
    conn.close()



def delete_influencer(id):
    conn = db_client()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Influencer WHERE id_influencer = %s", (id,))
    conn.commit()
    conn.close()

def get_empresas():
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Empresa")
    empresas = cursor.fetchall()
    conn.close()
    return empresas

def get_empresa(id):
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Empresa WHERE id_empresa = %s", (id,))
    empresa = cursor.fetchone()
    conn.close()
    return empresa

def create_empresa(empresa):
    conn = db_client()
    cursor = conn.cursor()
    query = """
        INSERT INTO Empresa (email, password)
        VALUES (%s, %s)
    """
    cursor.execute(query, (empresa.email, empresa.password))
    conn.commit()
    conn.close()

def update_empresa(id, empresa):
    conn = db_client()
    cursor = conn.cursor()
    query = """
        UPDATE Empresa
        SET nom = %s, descripcio = %s, email_contacto = %s, web = %s,
            ubicacio = %s, sector = %s
        WHERE id_empresa = %s
    """
    cursor.execute(query, (
        empresa.nombre, empresa.descripcion, empresa.email_contacto,
        empresa.web, empresa.ubicacion, empresa.sector, id
    ))
    conn.commit()
    conn.close()

def delete_empresa(id):
    conn = db_client()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Empresa WHERE id_empresa = %s", (id,))
    conn.commit()
    conn.close()

def verify_user(table: str, email: str, password: str):
    conn = db_client()
    cursor = conn.cursor(dictionary=True)
    query = f"SELECT * FROM {table} WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    conn.close()
    return user
