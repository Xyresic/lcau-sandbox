let map = L.map('map').setView([0, 0], 1);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: 'red',
    fillOpacity: 1,
    radius: 100
}).addTo(map);

let locations = []