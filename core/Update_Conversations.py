import psycopg2
from dotenv import load_dotenv
import os


def Update_Conversations(role: str,data: dict):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DBNAME")
    )
    cursor = connection.cursor()

    Role = role
    chat_id = data["Chat_id"]

    if role == "User":    
        Content = data["User_Input"]
    elif role == "AI":
        Content = data["AI_Output"]
    Query = """
    INSERT INTO conversat ions(role, content, chat_id)
    VALUES (%s, %s, %s);
    """

    cursor.execute(Query, (Role, Content, chat_id))
    connection.commit()
    cursor.close()
    return 


