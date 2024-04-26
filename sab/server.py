import socket
import requests
import json
import time

class VelibData:
    def __init__(self):
        self.last_request_time = 0
        self.data = None
    
    def fetch_data(self):
        current_time = time.time()
        if current_time - self.last_request_time < 300 and self.data:
            return self.data
        api_url = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
               self.data = response.json()
               self.last_request_time = current_time
               return self.data
            else:
               print("Erreur lors de la récupération des données Velib. Statut de réponse :", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la récupération des données Velib :", e)
        
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
            response = "HTTP/1.1 200 OK\nContent-Type: application/json\nAccess-Control-Allow-Origin: *\n\n" + json.dumps(data)
            socket_client.sendall(response.encode())
        else:
            error_message = "HTTP/1.1 500 Internal Server Error\nContent-Type: text/plain\n\nErreur lors de la récupération des données Velib."
            socket_client.sendall(error_message.encode())
        socket_client.close()
except KeyboardInterrupt:
    print("Interruption du serveur par l'utilisateur.")
except Exception as e:
    print("Erreur lors de l'exécution du serveur :", e)
finally:
    socket_server.close()
