import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { mapConfig, logUrl } from '.././shared/map.constants';

@Injectable({
  providedIn: 'root'
})
export class MapService {
  rootUrl = logUrl;
  constructor(private http: HttpClient) {}
  getData(): Observable<any[]> {
    return this.http.get<any[]>(this.rootUrl);
  }
}
