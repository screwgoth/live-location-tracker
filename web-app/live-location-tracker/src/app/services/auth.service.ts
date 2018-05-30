import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  rootUrl = 'http://20.20.5.105:8000/api/v1/users/login/';
  loggedUsername: string;
  loggedUserId: string;
  constructor(private http: HttpClient) { }

  loginUser(data) {
    return this.http.post(this.rootUrl, data);
  }
  setUserLoggedin(token, uname) {
  localStorage.setItem('user-token', token);
  }
  isLoggedin() {

    return !!localStorage.getItem('user-token');
  }
}
