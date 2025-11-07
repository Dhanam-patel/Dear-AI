import psycopg2
from dotenv import load_dotenv
import os


def Chat_Name_List ():
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DBNAME")
    )
    cursor = connection.cursor()
    Query = f"""
    SELECT chat_name FROM chat_history;
    """ 
    cursor.execute(Query)
    Chats = cursor.fetchall()   
    connection.commit()

    Query = f"""
    SELECT user_id FROM user_info;
    """ 
    cursor.execute(Query)
    Users_list = cursor.fetchall()   
    connection.commit()

    cursor.close()
    connection.close()
    return {"Chats": Chats, "Users": Users_list}


