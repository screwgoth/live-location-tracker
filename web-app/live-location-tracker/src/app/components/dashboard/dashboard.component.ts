import { Component, OnInit } from '@angular/core';

import { icon, latLng, marker, polyline, tileLayer, Map, circle, polygon } from 'leaflet';
import * as L from 'leaflet';
import { MapService } from '../../services/map.service';
import { mapConfig } from '../../shared/map.constants';
import { interval } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  map;
  mapinterval;
  center: L.LatLng;
  options = {
    layers: [
      tileLayer(mapConfig.tileLayer,
        {
          maxZoom: mapConfig.maxZoom,
          attribution: mapConfig.attribution,
          id: mapConfig.id
        })
    ],
    zoom: mapConfig.zoom,
    center: latLng(mapConfig.center_lat, mapConfig.center_long)
  };
  layers = [];
  latlngs: any[] = [];
  constructor(private service: MapService) { }

  ngOnInit() {
    // this.mapinterval = interval(1000).subscribe(x => {
      this.service.getData().subscribe(data => {
        if (this.latlngs.length === 0) {
            this.latlngs = data;
          } else {
            for (let i = 0; i < data.length; i++) {
                 this.latlngs.push(
              {
                'id': data[i]['id'],
                'lat': data[i]['lat'],
                'long': data[i]['long']
              }
            );
            }
         }
        this.load();
      });
    // });
  }
  load() {
    for (let i = 0; i < this.latlngs.length; i++) {
      this.layers.push(
        polyline([
          new L.LatLng(this.latlngs[0].lat, this.latlngs[0].long),
          new L.LatLng(this.latlngs[i].lat, this.latlngs[i].long)
        ]),
        circle([ this.latlngs[i].lat, this.latlngs[i].long], { radius: mapConfig.circle_radius })
      );
    }
  }
  onMapReady(map: Map) {
    this.map = map;
 }
}
