import mysql.connector
from mysql.connector import Error

def db_client():
    try:
        dbname = "fluence"  
        user = "root"
        password = "pirineus"  
        host = "localhost"
        port = 3306

        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname
        )

        return conn if conn.is_connected() else None

    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None
