window.addEventListener("load", fetchVelibData);

const map = L.map("map").setView([48.8566, 2.3522], 13);

const tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  minZoom: 13,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

function fetchVelibData() {
  fetch("http://localhost:5000/velib")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des données Velib.");
      }
      return response.json();
    })
    .then((data) => {
      data.forEach((station, index) => {
        console.log(data);
        const lat = station.coordonnees_geo.lat;
        const lon = station.coordonnees_geo.lon;
        const numbikesavailable = station.numbikesavailable;
        const numdocksavailable = station.numdocksavailable;
        const ebike = station.ebike;
        const mechanical = station.mechanical;
        const marker = L.marker([lat, lon]).addTo(map);

        // Créer le lien avec les informations de la station en tant que paramètres de requête
        const url = `/favoris?id_favoris=${station.stationcode}&id_user=123&nom=${station.name}&numbikesavailable=${numbikesavailable}&numdocksavailable=${numdocksavailable}&ebike=${ebike}&mechanical=${mechanical}`;

        const popupContent = `<b>${station.name}</b><br/>Vélos disponibles : ${station.numbikesavailable} <a href="${url}" data-index="${index}">Ajouter en favoris</a>`;
        marker.bindPopup(popupContent);
      });
    })
    .catch((error) => {
      console.error(error);
    });
}
