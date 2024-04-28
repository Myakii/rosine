window.addEventListener("load", fetchVelibData);

<<<<<<< HEAD
const map = L.map("map").setView([48.8566, 2.3522], 13);

=======
//On importe la carte de la bibliothèque leaflet et on régle un la setView pour avoir une vue sur paris 
const map = L.map("map").setView([48.8566, 2.3522], 13);

//On initialise une couche de tuiles OpenStreetMap avec une attribution spécifiée et l'ajoute à la carte Leaflet, avec un niveau de zoom minimum de 13.
>>>>>>> 6bd867c4cb15006181af7c1cf2bbc185045258be
const tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  minZoom: 13,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

function fetchVelibData() {
<<<<<<< HEAD
=======

  //On récupère les données à l'url définie dans app.py
>>>>>>> 6bd867c4cb15006181af7c1cf2bbc185045258be
  fetch("http://localhost:5000/velib")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des données Velib.");
      }
      return response.json();
    })
<<<<<<< HEAD
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
=======
    // On récupère la latitude et la longétitude des stations
    .then((data) => {
      console.log(data);
      data.forEach((station) => {
        const lat = station.coordonnees_geo.lat;
        const lon = station.coordonnees_geo.lon;
        console.log(lat, lon);
        const marker = L.marker([lat, lon]).addTo(map);
        
         //Affiche un popup avec les informations de la station
        const popupContent = `<b>${station.name}</b><br/>Vélos disponibles : ${station.numbikesavailable}`;
>>>>>>> 6bd867c4cb15006181af7c1cf2bbc185045258be
        marker.bindPopup(popupContent);
      });
    })
    .catch((error) => {
      console.error(error);
    });
}
