let map = L.map('map').setView([0, 0], 1);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

for (let location of locations) {
    circle = L.circle(location.slice(0, 2), {
        color: 'red',
        fillColor: 'red',
        fillOpacity: 1,
        radius: 1000
    }).addTo(map);

    circle.bindPopup(location[2]);
}
