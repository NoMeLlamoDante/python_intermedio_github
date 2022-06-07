import re
import psycopg2

def get_connection():
    conn = None
    cur = None 
    try:
        conn = psycopg2.connect("dbname = python_intermedio_db user = postgres password= JlSIU@|u1Z3WT1yK")
        cur = conn.cursor()
    except Exception as e:
        print(e)
    
    return conn, cur

def condition(data):
    if type(data) == int:
        return f"id = '{data}'"
    # Search is Text would be an username or a email
    elif type(data) == str:
        #Mail
        if isMail(data):
            return f"email = '{data}'"
        #Username
        else:
            return f"username = '{data}'"


def key_conditions(**kwargs):
    conditions = ""
    # Only if exist conditions
    if(kwargs):
        for key, value in kwargs.items():
            # add AND statement if exist more than 1 Condition
            if len(conditions)>0:
                conditions+=', '
            # Add Condition statement
            conditions+= f"{key} = '{value}' "
    return conditions

def isMail(email):
    # Regular Expresion for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
    #check
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False