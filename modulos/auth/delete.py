from pickle import TRUE
from typing import Type, final
import psycopg2
from .connection import get_connection, query_conditions

def delete_user(**kwargs):
    conn, cur = get_connection()
    result = None
    try:
        conditions = query_conditions(**kwargs)
        if conditions:
            query = f"DELETE FROM usuarios {conditions};"
            cur.execute(query)
            result = TRUE
    except psycopg2.Error as e:
        result = e
    except TypeError as e:
        result = e
    finally:    
        conn.commit()
        cur.close()
        conn.close()
    return result
