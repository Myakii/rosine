from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_database_connection():
    return mysql.connector.connect(
        user='root',
        password='',
        database='velib'
    )

def execute_query(query):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

@app.route('/')
def index():
    return "<p>Bienvenue</p>"

@app.post('/favoris')
def add_favorite():
    data = request.json
    id_favoris = data.get('id_favoris')
    id_user = data.get('id_user')
    velib_disponible = data.get('velib_disponible')
    adresse = data.get('adresse')
    velib_elect = data.get('velib_elect')
    velib_classic = data.get('velib_classic')
    place_disponible = data.get('place_disponible')

    query = "INSERT INTO favoris (id_favoris, id_user, adresse, place_disponible, velib_classic, velib_elect, velib_disponible) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, (id_favoris, id_user, adresse, place_disponible, velib_classic, velib_elect, velib_disponible))

    return jsonify({"message": "Favorite ajouté avec succès"})

if __name__ == "__main__":
    app.run(debug=True)
