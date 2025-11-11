import psycopg2
from dotenv import load_dotenv
import os


def Deleting_chats (data: str):
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
    DELETE FROM chats 
    WHERE chat_id = '{Chat_id}';
    """

    Chats = cursor.execute(Query)
    connection.commit()
    cursor.close()
    connection.close()
    return Chats


