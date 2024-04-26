from database import connect_to_database

def add_favorite_with_json_id(user_id, json_file_id):
    # Charger le fichier JSON correspondant à l'ID
    try:
        with open(f'{json_file_id}.json', 'r') as file:
            favorite_data = json.load(file)
    except FileNotFoundError:
        return {"message": "Page introuvable"}, 404

    # Appeler la fonction pour ajouter le favori
    add_favorite(user_id, favorite_data)

    return {"message": "Favorite ajouté avec succès"}

def delete_favorite(user_id, favorite_id):
    # Fonction pour supprimer un favori
    if favorite:
        # Supprimer le favori de la base de données
        session.delete(favorite)
        session.commit()
        print("Favori supprimé avec succès.")
    else:
        print("Aucun favori trouvé.")

def get_favorites(user_id):
    # Fonction pour récupérer les favoris d'un utilisateur
    if favorites:
        return favorites
    else:
        return []

favorites = get_favorites(user_id)
for favorite in favorites:
    print(favorite.id, favorite.name)
