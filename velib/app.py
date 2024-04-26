from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="hostname",
    user='root',
    password='',
    database='velib'
)
cursor = connection.cursor()

@app.route('/favorites', methods=['POST'])
def add_favorite():
    data = request.json
    user_id = data.get('user_id')
    favorite_data = data.get('favorite_data')

    query = "INSERT INTO favorites (user_id, favorite_data) VALUES (%s, %s)"
    cursor.execute(query, (user_id, favorite_data))
    connection.commit()

    return jsonify({"message": "Favorite ajouté avec succès"})

@app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    query = "DELETE FROM favorites WHERE id = %s"
    cursor.execute(query, (favorite_id,))
    connection.commit()

    return jsonify({"message": "Favori supprimé avec succès"})

@app.route('/favorites/<int:user_id>', methods=['GET'])
def get_user_favorites(user_id):
    query = "SELECT * FROM favorites WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    favorites = cursor.fetchall()

    return jsonify(favorites)

if __name__ == "__main__":
    app.run(debug=True)
