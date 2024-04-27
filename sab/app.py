from flask import Flask, render_template, jsonify
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

if __name__ == "__main__":
    app.run(debug=True)
