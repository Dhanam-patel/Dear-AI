import psycopg2
from psycopg2 import sql, IntegrityError
from dotenv import load_dotenv
import os

def Create_Users(data: dict):
    load_dotenv()
    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=5432,
        dbname=os.getenv("DBNAME")
    )
    cursor = connection.cursor()

    try:
        insert_query = """
            INSERT INTO user_info (first_name, last_name, age, gender, city, username, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            data["FirstName"].title(),
            data["LastName"].title(),
            data["Age"],
            data["Gender"].lower(),
            data["City"].title(),
            data["Username"],
            data["Email"]
        )
        cursor.execute(insert_query, values)
        connection.commit()
    except IntegrityError as e:
        connection.rollback()
        if "user_info_username_key" in str(e):
            raise ValueError("Username already exists.") from e
        else:
            raise
    finally:
        cursor.close()
        connection.close()
