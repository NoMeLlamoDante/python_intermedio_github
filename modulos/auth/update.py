import psycopg2
from .connection import get_connection,condition,key_conditions

def update_user(search,**kwargs):
    conn, cur = get_connection()
    result = None
    try:

        query = f"UPDATE usuarios SET {key_conditions(**kwargs)} WHERE {condition(search)};"
        result = cur.execute(query);
        conn.commit()
        result = True
    except psycopg2.Error as e:
        result = e
    finally:
        cur.close()
        conn.close()
    return result


    
 

def isMail(email):
    # Regular Expresion for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
    #check
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False