import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  rootUrl = environment.API_URL;
  constructor (private http: HttpClient) { }

  registerUser(data) {
    console.log(data);
   return this.http.post(`${this.rootUrl}register/`, data);
  }
}
