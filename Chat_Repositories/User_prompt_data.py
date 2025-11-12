import psycopg2
from dotenv import load_dotenv
import os


def User_prompt_data (data: str):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=5432,
        dbname=os.getenv("DBNAME")
    )

    Chat_id = data

    cursor = connection.cursor()
    Query = f"""
    SELECT ui.age, ui.gender 
    FROM user_info ui
    INNER JOIN chats c ON ui.user_id = c.user_id
    WHERE chat_id = '{Chat_id}';
    """ 
    cursor.execute(Query)
    Chats = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return Chats


