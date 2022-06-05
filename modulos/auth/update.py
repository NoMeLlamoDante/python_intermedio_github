#Regex
import re
from typing import final
import psycopg2
from .connection import get_connection

def update_user(search,**kwargs):
    conn, cur = get_connection()

    # Update Info
    update_info = None
    # Only if exist conditions
    if(kwargs):
        update_info = ''
        for key, value in kwargs.items():
            # add ',' statement if exist more than 1 Condition
            if len(update_info)>0:
                update_info+=", "
            # Add Condition statement
            update_info+= f"{key} = '{value}' "

    # Search condition
    search_condition = None
    # Search is an number means ID
    if type(search) == int:
        search_condition = f"id = {search}"
    # Search is Text would be an username or a email
    elif type(search) == str:
        #Mail
        if isMail(search):
            search_condition = f"email = {search}"
        else:
            search_condition = f"username = {search}"
    
    result = None
    try:
        if update_info and search_condition:
            query = f"UPDATE usuarios SET {update_info} WHERE {search_condition};"
            result = cur.execute(query);
            conn.commit()
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