import psycopg2
import dotenv
import os

def Create_Chats(data: dict):
    import psycopg2
from dotenv import load_dotenv
import os


def Create_Chats (data: dict):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DBNAME")
    )

    Chat_Name = data["Chat_Name"]
    User_id = data["User_id"]

    cursor = connection.cursor()

    Query = f"""
    INSERT INTO chat_history (chat_name, created_time, user_id)
    VALUES ('{Chat_Name}', NOW(), '{User_id}');
    """

    Chats = cursor.execute(Query)
    connection.commit()
    cursor.close()
    connection.close()
    return Chats


