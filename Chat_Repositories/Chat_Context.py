import psycopg2
from dotenv import load_dotenv
import os


def Retrieve_Chat_History (data: str):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DBNAME")
    )

    Chat_id = data

    cursor = connection.cursor()

    Query = f"""
    SELECT * FROM conversations 
    WHERE chat_id = '{Chat_id}' ORDER BY created_at;
    """

    Retrieved_Data = cursor.execute(Query)
    Retrieved_Data = cursor.fetchall()  
    cursor.close()
    connection.close()
    return Retrieved_Data


