from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Bienvenue</p>"

def get_database_connection():
    return mysql.connector.connect(
        user='root',
        password='',
        database='velib'
    )

def execute_query(query, data=None):
    connection = get_database_connection()
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        return cursor
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

@app.route('/favoris', methods=['POST'])
def add_favorite():
    data = request.json
    user_id = data.get('id_user')
    nom = data.get('nom')
    adresse = data.get('adresse')
    capacite = data.get('capacite')
    code = data.get('code')
    paiement = data.get('paiement')

    query = "INSERT INTO favoris (id_user, nom, adresse, capacite, code, paiement) VALUES (%s, %s, %s, %s, %s, %s)"
    execute_query(query, (user_id, nom, adresse, capacite, code, paiement))

    return jsonify({"message": "Favorite ajouté avec succès"})

@app.route('/favoris/<int:id_favoris>', methods=['DELETE'])
def delete_favorite(id_favoris):
    query = "DELETE FROM favoris WHERE id_favoris = %s"
    execute_query(query, (id_favoris,))

    return jsonify({"message": "Favori supprimé avec succès"})

@app.route('/favoris/<int:user_id>', methods=['GET'])
def get_user_favoris(user_id):
    query = "SELECT * FROM favoris WHERE id_user = %s"
    cursor = execute_query(query, (user_id,))
    favoris = cursor.fetchall() 
    cursor.close()
    return jsonify(favoris)

if __name__ == "__main__":
    app.run(debug=True)
