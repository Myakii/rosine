// Définir la carte Leaflet
var map = L.map('map').setView([48.8566, 2.3522], 13); // Coordonnées de Paris

// Ajouter un calque de tuiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Fonction pour ajouter des marqueurs à partir des données Velib
function addVelibMarkers(data) {
    data.forEach(function(velib) {
        var marker = L.marker([velib.geometry.coordinates[1], velib.geometry.coordinates[0]]).addTo(map);
        marker.bindPopup("<b>Station Velib</b><br>" + velib.fields.station_name);
    });
}

// Récupérer les données Velib via une requête AJAX
fetch('http://localhost:3333')
    .then(response => response.json())
    .then(data => addVelibMarkers(data))
    .catch(error => console.error('Erreur lors de la récupération des données Velib:', error));
