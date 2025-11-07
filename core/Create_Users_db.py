import psycopg2
from dotenv import load_dotenv
import os


def Create_Users (data: dict):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DBNAME")
    )
    cursor = connection.cursor()

    First_name = data["FirstName"]
    Last_name = data["LastName"]
    Age = data["Age"]
    Gender = data["Gender"]
    City = data["City"]
    Username = data["Username"]

    Query = f"""
    INSERT INTO user_info(first_name, last_name, age, gender, city, username)
    VALUES ('{First_name}', '{Last_name}', {Age}, '{Gender}', '{City}', '{Username}');
    """
    cursor.execute(Query)
    connection.commit()
    cursor.close()
    connection.close()
    return 


