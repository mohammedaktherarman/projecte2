import mysql.connector

def db_client():
    dbname = "fluence"
    user = "root"
    password = "pirineus"
    host = "localhost"
    port = 3306

    print("Iniciando conexión a la base de datos...")
    try:
        print(f"Intentando conectar a MySQL en {host}:{port} con usuario '{user}' a la base '{dbname}'")
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            charset="utf8mb4"
        )
        print("Conexión exitosa a la base de datos")
        return conn

    except mysql.connector.InterfaceError as ie:
        print(f"Error de interfaz: ¿MySQL está corriendo? Detalles: {ie}")
        raise  # Re-lanzamos para que no pase silencioso

    except mysql.connector.ProgrammingError as pe:
        print(f"Error de programación: revisa las credenciales y base de datos. Detalles: {pe}")
        raise

    except mysql.connector.DatabaseError as de:
        print(f"Error en la base de datos: {de}")
        raise

    except Exception as e:
        print(f"Error inesperado durante conexión: {e}")
        raise
