import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IRegister, ILogin } from '../../models/register.model';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  userLoginForm: FormGroup;
  userLoginData: ILogin = {
    username: '',
    password: ''
  };
  invalidLoginerror: string;
  constructor(private fb: FormBuilder, private service: AuthService, private router: Router) {
    this.createForm();
  }

  ngOnInit() {
    console.log(this.service.isLoggedin());
  }
  createForm() {
    this.userLoginForm = this.fb.group({
      'username': ['', Validators.required],
      'password': ['', [Validators.required, Validators.minLength(5)]]
    });
  }
  loginUserData(form: FormGroup) {
    const uname = form.value['username'];
    const pass = form.value['password'];
    this.userLoginData.username = uname;
    this.userLoginData.password = pass;
    this.service.loginUser(this.userLoginData).subscribe(result => {
      this.service.loggedUserId = result['token'];
      this.service.loggedUsername = result['username'];
      this.service.setUserLoggedin(this.service.loggedUserId, this.service.loggedUsername);
      this.router.navigate(['dashboard']);
    }, err => {
      this.invalidLoginerror = err['error'].message;
    });
    this.userLoginForm.reset();
  }

}
