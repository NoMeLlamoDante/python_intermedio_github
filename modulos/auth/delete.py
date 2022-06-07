import psycopg2
from .connection import get_connection, condition

def delete_user(search):
    conn, cur = get_connection()
    result = None
    try:
        query = f"DELETE FROM usuarios WHERE {condition(search)};"
        cur.execute(query)
        result = True
    except psycopg2.Error as e:
        result = e
    except TypeError as e:
        result = e
    finally:    
        conn.commit()
        cur.close()
        conn.close()
    return result
