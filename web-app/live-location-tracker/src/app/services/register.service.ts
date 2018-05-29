import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  rootUrl = 'http://20.20.5.105:8000/api/v1/users/';
  constructor (private http: HttpClient) { }

  registerUser(data) {
    console.log(data);
   return this.http.post(`${this.rootUrl}register/`, data);
  }
}
