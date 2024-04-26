from flask import Flask, request, jsonify
from favorites import add_favorite, delete_favorite, get_favorites
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Bienvenue</p>"

@app.route('/add_favorite', methods=['POST'])
def add_favorite_route():
    data = request.get_json()
    # Appel à la fonction pour ajouter un favori
    # Exemple : add_favorite(data['user_id'], data['favorite_data'])
    return jsonify({"message": "Favorite added successfully"})

@app.route('/delete_favorite/<user_id>/<favorite_id>', methods=['DELETE'])
def delete_favorite_route(user_id, favorite_id):
    # Appel à la fonction pour supprimer un favori
    # Exemple : delete_favorite(user_id, favorite_id)
    return jsonify({"message": "Favorite deleted successfully"})

@app.route('/get_favorites/<user_id>', methods=['GET'])
def get_favorites_route(user_id):
    # Appel à la fonction pour récupérer les favoris d'un utilisateur
    # Exemple : favorites = get_favorites(user_id)
    # return jsonify(favorites)
    return jsonify({"message": "Favorites retrieved successfully"})

if __name__ == "__main__":
    app.run(debug=True)
