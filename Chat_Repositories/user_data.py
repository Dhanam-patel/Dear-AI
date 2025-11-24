import psycopg2
from dotenv import load_dotenv
import os


def users_data (username: str):
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
    SELECT user_id FROM user_info
    WHERE username = '{username}';
    """ 
    cursor.execute(Query)
    Users_list = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return {"Users": Users_list}


