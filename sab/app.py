from flask import Flask, render_template, jsonify, request, redirect
import mysql.connector
import json
from server import VelibData

app = Flask(__name__)
velib_data = VelibData()

@app.route("/")
def accueil():
    return render_template("index.html")

#récupération des données à une autre route en important la variable depuis server.py, lancé en amont et qui aura récupéré les données de l'api
@app.route("/velib")
def velib():
    data = get_velib_data()
    response = jsonify(data)
    #ajout des headers pour les autorisations CORS
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def get_velib_data():
    data = velib_data.fetch_data()
    if data:
        return data
    else:
        return {"error": "Erreur lors de la récupération des données Velib."}

def get_database_connection():
    return mysql.connector.connect(
        user='root',
        password='',
        database='velib'
    )

def execute_query(query, data=None):
    connection = get_database_connection()
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    connection.commit()
    connection.close()

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")

@app.route('/favoris', methods=['POST'])
def add_favorite():
    connection = get_database_connection()
    data = request.json
    id_favoris = data.get('id_favoris')
    id_user = data.get('id_user')
    nom = data.get('nom')
    data_json = json.dumps(data.get('data_json'))

    query = "INSERT INTO favoris (id_favoris, id_user, nom, data_json) VALUES (%s, %s, %s, %s)"
    execute_query(query, (id_favoris, id_user, nom, data_json))
    connection.close()

    return jsonify({"message": "Favori ajouté avec succès"})

@app.delete('/favoris/<int:id_favoris>')
def delete_favorite(id_favoris):
    connection = get_database_connection()
    query = "DELETE FROM favoris WHERE id_favoris = %s"
    execute_query(query, (id_favoris,))
    connection.close()

    return jsonify({"message": "Favori supprimé avec succès"})

@app.route('/favoris/modification/<int:id_favoris>', methods=['GET', 'POST'])
def update_favorites(id_favoris):
    if request.method == 'POST':
        nom = request.form.get('nom')
        connection = get_database_connection()
        cursor = connection.cursor()
        query = "UPDATE favoris SET nom = %s WHERE id_favoris = %s"
        cursor.execute(query, (nom, id_favoris))
        connection.commit()
        connection.close()

        return redirect('/favoris/lire/{}'.format(id_favoris))
    else:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM favoris WHERE id_favoris = %s"
        cursor.execute(query, (id_favoris,))
        favoris = cursor.fetchone()
        connection.close()

        return render_template('modification.html', favoris=favoris)


@app.route('/favoris/lire/<int:id_favoris>')
def afficher_favoris(id_favoris):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM favoris WHERE id_favoris = %s"
    cursor.execute(query, (id_favoris,))
    favoris = cursor.fetchone()
    connection.close()
    return render_template('favoris.html', favoris=favoris)


# Configuration MySQL à modifier avec vraie bdd
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

@app.route("/")
def homepage():
    # Récupère le prenom dans la session
    first_name = session["first_name"] if "first_name" in session else None
    local_user = request.cookies.get("local_user")
    # Affichage
    return render_template("index.html.jinja", first_name=first_name, local_user=local_user)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Récupère données formulaire
        username = request.form["username"]
        password = request.form["password"]

        # Connexion à la bdd
        cur = mysql.connection.cursor()

        # Vérifie si user existe déjà
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            return "Cet utilisateur existe déjà !"
        else:
            # Insertion dans la bdd
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()

            # Fermeture du curseur
            cur.close()

            return redirect(url_for("homepage"))

    return render_template("register.html.jinja")

# Route de connexion
@app.route("/login", methods=["POST"])
def login():

    # Prépare la réponse
    response = make_response(redirect(url_for("homepage")))
    # Récupère les infos
    first_name = request.form["first_name"]
    local_user = "local_user" in request.form
    # Gestion de la session
    session["first_name"] = first_name

#Vérifie si le user a coché la case "rester connecté", définit cookie pour user si la réponse est oui
    if local_user:
        response.set_cookie("local_user", first_name)
#Supprime cookie sinon
    else:
        response.delete_cookie("local_user")
    # Redirection
    return response

# Déconnexion
@app.route("/deconnexion")
def deconnexion():
    # Retire la clé prenom de la session
    session.pop("first_name", None)
    # Redirection
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(debug=True)
