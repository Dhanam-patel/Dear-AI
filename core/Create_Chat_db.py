import psycopg2
from dotenv import load_dotenv
import os


def Create_Chats (data: dict):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=5432,
        dbname=os.getenv("DBNAME")
    )

    Chat_Name = data["Chat_Name"]
    User_id = data["User_id"]

    cursor = connection.cursor()

    Query = f"""
    INSERT INTO chats (chat_name, created_at, user_id)
    VALUES ('{Chat_Name}', NOW(), '{User_id}');
    """

    Chats = cursor.execute(Query)
    connection.commit()
    cursor.close()
    connection.close()
    return Chats


