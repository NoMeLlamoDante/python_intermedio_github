import email
import psycopg2
from .connection import get_connection, condition
# https://www.psycopg.org/docs/module.html#exceptions

def read_users():
    conn, cur = get_connection()
    query = f"SELECT id, username, email, status FROM usuarios;"
    try: 
        cur.execute(query)
        # More than 1 Result
        result = cur.fetchall()
    except psycopg2.Error as e:
        result = e
    finally:
        cur.close()
        conn.close()
    return result

def read_user(search):
    conn, cur = get_connection()
    # query = f"SELECT id, username, password, email, status FROM usuarios WHERE {query_conditions('AND ',**kwargs)};"
    # acording to Search parameter
    query = f"SELECT id, username, password, email, status FROM usuarios WHERE { condition(search) };"
    try:
        cur.execute(query)
        # Just 1 Result
        result = cur.fetchone();
    except psycopg2.Error as e:
        result = e
    finally:
        cur.close()
        conn.close()
    return result