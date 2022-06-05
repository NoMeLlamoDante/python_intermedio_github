from getpass import getuser
import psycopg2
import dbinfo
def getUser(userID):
    conn = psycopg2.connect(dbinfo.info)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuarios WHERE ID ={userID} ;")
    print(cur.fetchone())
    cur.close()
    conn.close()

getUser(50);