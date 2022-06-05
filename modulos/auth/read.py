import psycopg2
from .connection import get_connection, query_conditions
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

def read_user(**kwargs):
    conn, cur = get_connection()
    query = f"SELECT id, username, email, status FROM usuarios {query_conditions(**kwargs)};"
    # if not conditions
    if not kwargs:
        return None
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