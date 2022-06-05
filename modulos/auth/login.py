import psycopg2
from .connection import get_connection

def is_authenticated(usuario, password):
    conn, cur = get_connection()
    result = None
    try:
        consulta = f"SELECT username, email FROM usuarios WHERE username=\'{usuario}\' AND password = \'{password}\';"
        cur.execute(consulta)
        usuario_encontrado = cur.fetchone()
        if usuario_encontrado:
            result = usuario_encontrado    
    except psycopg2.Error as e:
        result = e
    except TypeError as e:
        result = e
    finally:
        cur.close()
        conn.close()
    return result