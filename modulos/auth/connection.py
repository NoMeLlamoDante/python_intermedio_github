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

def query_conditions(**kwargs):
    conditions = ""
    # Only if exist conditions
    if(kwargs):
        conditions += "WHERE "
        for key, value in kwargs.items():
            # add AND statement if exist more than 1 Condition
            if len(conditions)>6:
                conditions+="AND "
            # Add Condition statement
            conditions+= f"{key} = '{value}' "
    return conditions