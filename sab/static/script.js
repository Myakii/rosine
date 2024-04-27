window.addEventListener("load", fetchVelibData);

const map = L.map("map").setView([48.8566, 2.3522], 13);

const tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  minZoom: 13,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

function fetchVelibData() {
  //On récupère les données à l'url définie dans app.py
  fetch("http://localhost:5000/velib")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des données Velib.");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      data.forEach((station) => {
        const lat = station.coordonnees_geo.lat;
        const lon = station.coordonnees_geo.lon;
        console.log(lat, lon);
        const marker = L.marker([lat, lon]).addTo(map);

        const popupContent = `<b>${station.name}</b><br/>Vélos disponibles : ${station.numbikesavailable}`;
        marker.bindPopup(popupContent); //Affiche un popup avec les informations de la station
      });
    })
    .catch((error) => {
      console.error(error);
    });
}
