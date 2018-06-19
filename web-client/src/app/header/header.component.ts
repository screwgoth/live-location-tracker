import { Component, OnInit } from '@angular/core';
import { AuthService } from '.././services/auth.service';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  public isLoggedIn: boolean = false;
  constructor(private service: AuthService) { }

  ngOnInit() {
    this.isLoggedIn = this.service.isLoggedin();
  }
  signOut() {
   localStorage.removeItem('user-token');
  }
}
