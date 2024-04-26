from flask import Flask
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    connection = mysql.connector.connect(
        host="hostname",
        user='root',
        password='',
        database='velib'
    )
    return connection

def insert_favorite(user_id, favorite_data):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO favorites (user_id, favorite_data) VALUES (%s, %s)"
    cursor.execute(query, (user_id, favorite_data))
    connection.commit()

    cursor.close()
    connection.close()

def delete_favorite(user_id, favorite_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "DELETE FROM favorites WHERE user_id = %s AND id = %s"
    cursor.execute(query, (user_id, favorite_id))
    connection.commit()

    cursor.close()
    connection.close()

def get_user_favorites(user_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM favorites WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    favorites = cursor.fetchall()

    cursor.close()
    connection.close()

    return favorites

if __name__ == "__main__":
    app.run(debug=True)
