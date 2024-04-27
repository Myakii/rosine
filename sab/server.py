import socket
import json
import time
import requests

class VelibData:
    #utilisation d'une classe pour une question de clead code
    def __init__(self):
        self.last_request_time = 0
        self.data = None
    
    def fetch_data(self):
        #comparaison en amont avec la date du dernier appel, s'il date de moins de 300s, on retourne data
        current_time = time.time()
        if current_time - self.last_request_time < 300 and self.data:
            return self.data
        #utilisation de l'opendata de Velib et non Paris car celui de Paris bloquait les requetes à 100 stations
        api_url = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"
        #sinon, on appelle l'api, stocke la date actuelle puis les données récupérées
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                self.last_request_time = current_time
                self.data = response.json()
                return self.data
        except:
            print("Erreur lors de la récupération des données Velib.")
        
        return None

try:
    velib_data = VelibData()
    socket_server = socket.socket()
    host = socket.gethostname()
    port = 3000
    socket_server.bind((host, port))
    socket_server.listen(5)
    print("Serveur en écoute sur le port 3000.")

    while True:
        socket_client, addr = socket_server.accept()
        data = velib_data.fetch_data()
        if data:
            socket_client.sendall(json.dumps(data).encode())
        else:
            socket_client.sendall("Erreur lors de la récupération des données Velib.")
        socket_client.close()
except KeyboardInterrupt: #Pas forcément utile mais c'est apparemment une bonne pratique
    print("Interruption du serveur par l'utilisateur.")
except Exception:
    print("Erreur lors de l'exécution du serveur.")
finally:
    socket_server.close()
