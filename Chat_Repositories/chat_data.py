import psycopg2
from dotenv import load_dotenv
import os


def chats_data (id: str, name: str):
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
    SELECT chat_id FROM chats
    WHERE user_id = '{id}' and chat_name = '{name}';
    """ 
    cursor.execute(Query)
    Chat_id = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return {"Chat_id": Chat_id}


