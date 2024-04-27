from flask import Flask, request, jsonify, render_template
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
    velib_elect = data.get('velib_elect')
    velib_classic = data.get('velib_classic')
    adresse = data.get('adresse')
    place_disponible = data.get('place_disponible')

    query = "INSERT INTO favoris (id_favoris, id_user, velib_disponible, velib_elect, velib_classic, adresse, place_disponible) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, (id_favoris, id_user, velib_disponible, velib_elect, velib_classic, adresse, place_disponible))

    return jsonify({"message": "Favorite ajouté avec succès"})

@app.route('/favoris/<int:id_favoris>', methods=['DELETE'])
def delete_favorite(id_favoris):
    query = "DELETE FROM favoris WHERE id_favoris = %s"
    execute_query(query, (id_favoris,))

    return jsonify({"message": "Favori supprimé avec succès"})

@app.route('/favoris/modification/<int:id_favoris>', methods=['POST'])
def update_favorites(id_favoris):
    data = request.json
    id_user = data.get('id_user')
    velib_disponible = data.get('velib_disponible')
    adresse = data.get('adresse')
    velib_elect = data.get('velib_elect')
    velib_classic = data.get('velib_classic')
    place_disponible = data.get('place_disponible')

    query = "INSERT INTO favoris (id_favoris, id_user, velib_disponible, velib_elect, velib_classic, adresse, place_disponible) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, (id_favoris, id_user, velib_disponible, velib_elect, velib_classic, adresse, place_disponible))

    return jsonify({"message": "Favorite modifié avec succès"})


@app.get('/favoris/lire/<int:user_id>')
def get_user_favoris(user_id):
    query = "SELECT * FROM favoris WHERE id_user = %s"
    cursor = execute_query(query, (user_id,))
    favoris = cursor.fetchall()
    cursor.close()
    favoris_list = []
    for fav in favoris:
        favoris_list.append({
            'id_favoris': fav[0],
            'id_user': fav[1],
            'nom': fav[2],
            'adresse': fav[3],
            'capacite': fav[4],
            'code': fav[5],
            'paiement': fav[6]
        })
    print(favoris_list)

if __name__ == "__main__":
    app.run(debug=True)
