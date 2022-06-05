import psycopg2
from .connection import get_connection


def singIn(user, password, email):
    conn, cur = get_connection()
    result = None
    try:
        consulta = f"INSERT INTO usuarios(username, password, email, status) VALUES ('{user}', '{password}', '{email}', '0') RETURNING True;"
        cur.execute(consulta)
        if cur.rowcount > 0:
            result = user
    except psycopg2.Error as e:
        result = e
    except TypeError as e:
        result = e
    finally: 
        conn.commit()
        cur.close()
        conn.close()
    return result