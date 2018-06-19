export const access_token = `pk.eyJ1IjoicmFodWxnb3JlMzQiLCJhIjoiY2podTNvaWs0MGtmNDNwcDAweWJtc3gxdSJ9.
OBdwI0YJqrMP8Dsx-BZbGQ`;
export const mapConfig = {
tileLayer: `https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?
access_token=${access_token}`,
maxZoom: 18,
attribution: `Map data &copy; <a href="https://www.openstreetmap.org/">
OpenStreetMap</a> contributors,<a href="https://creativecommons.org/licenses/
by-sa/2.0/">CC-BY-SA</a>,Imagery © <a href="https://www.mapbox.com/">Mapbox</a>`,
id: 'mapbox.streets',
zoom: 10.5,
circle_radius: 20,
center_lat: 18.6571,
center_long: 73.7659,
access_token: `pk.eyJ1IjoicmFodWxnb3JlMzQiLCJhIjoiY2podTNvaWs0MGtmNDNwcDAweWJtc3gxdSJ9.
OBdwI0YJqrMP8Dsx-BZbGQ`
};
export const logUrl = 'http://20.20.5.105:8000/api/v1/location/log/';

