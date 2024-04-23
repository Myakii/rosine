const map = L.map('map').setView([48.8566, 2.3522], 13);

	const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 13,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	}).addTo(map);


// Récupérer les données sur les stations Velib depuis l'API
fetch('https://opendata.paris.fr/explore/dataset/velib-disponibilite-en-temps-reel/api/?disjunctive.name&disjunctive.is_installed&disjunctive.is_renting&disjunctive.is_returning&disjunctive.nom_arrondissement_communes')
    .then(response => response.json())
    .then(data => {
        // Parcourir les données et ajouter des marqueurs pour chaque station Velib
        data.data.stations.forEach(station => {
            const marker = L.marker([station.lat, station.lon]).addTo(map);
            marker.bindPopup(`<b>${station.name}</b><br/>${station.address}`);
        });
    })
    .catch(error => {
        console.error('Erreur lors de la récupération des données Velib :', error);
    });
