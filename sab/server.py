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
    port = 3333
    socket_server.bind((host, port))
    socket_server.listen(5)
    print("Serveur en Ã©coute sur le port 3333.")

    while True:
        socket_client, addr = socket_server.accept()
        data = velib_data.fetch_data()
        if data:
            socket_client.sendall(json.dumps(data).encode())
        else:
            socket_client.sendall("Erreur lors de la récupération des données Velib.")
        socket_client.close()
except KeyboardInterrupt:
    print("Interruption du serveur par l'utilisateur.")
except Exception:
    print("Erreur lors de l'exécution du serveur.")
finally:
    socket_server.close()
