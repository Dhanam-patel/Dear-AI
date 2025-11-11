import psycopg2
from dotenv import load_dotenv
import os


def User_Name_List ():
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=5432,
        dbname=os.getenv("DBNAME")
    )
    cursor = connection.cursor()
    Query = f"""
    SELECT user_id, username FROM user_info;
    """ 
    cursor.execute(Query)
    Users_list = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return {"Users": Users_list}


