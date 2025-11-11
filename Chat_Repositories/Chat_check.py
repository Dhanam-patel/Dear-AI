import psycopg2
from dotenv import load_dotenv
import os


def Chat_Name_List ():
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
    SELECT chat_name FROM chats;
    """ 
    cursor.execute(Query)
    Chats = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return {"Chats": Chats}


