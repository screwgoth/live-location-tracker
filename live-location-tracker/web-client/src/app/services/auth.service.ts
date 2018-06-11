import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  rootUrl = environment.API_URL;
  loggedUsername: string;
  loggedUserId: string;
  constructor(private http: HttpClient) { }

  loginUser(data) {
    return this.http.post(`${this.rootUrl}login/`, data);
  }
  setUserLoggedin(token, uname) {
  localStorage.setItem('user-token', token);
  }
  isLoggedin() {

    return !!localStorage.getItem('user-token');
  }
}
