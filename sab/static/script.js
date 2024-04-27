//execution de fetchVelibData au chargement de la page pour les afficher directement sur la map
window.addEventListener("load", fetchVelibData);

const map = L.map("map").setView([48.8566, 2.3522], 13);

const tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  minZoom: 13,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

function fetchVelibData() {
  //on récupère les données à l'url définie dans app.py
  fetch("http://localhost:5000/velib")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des données Velib.");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      data.data.stations.forEach((station) => {
        const lat = station.lat;
        const lon = station.lon;
        console.log(lat, lon);
        L.marker([lat, lon]).addTo(map);
      });
    })
    .catch((error) => {
      console.error(error);
    });
}
