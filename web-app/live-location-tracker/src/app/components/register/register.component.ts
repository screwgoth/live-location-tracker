import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IRegister } from '../../models/register.model';
import { RegisterService } from '../../services/register.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  userForm: FormGroup;
  data: IRegister = {
    username: '',
    email: '',
    password: ''
  };
  submitUserAlert: string;
  errorSubmitAlert: string;
  constructor(private fb: FormBuilder, private service: RegisterService) {
    this.createForm();
  }

  ngOnInit() {
  }
  createForm() {
    this.userForm = this.fb.group({
      'username': ['', [Validators.required]],
      'email': ['', [Validators.required, Validators.email]],
      'password': ['', [Validators.required, Validators.minLength(5)]]
    });
  }
  registerUser(form) {
    console.log(form.value);
    this.data = {
      username: form.value['username'],
      email: form.value['email'],
      password: form.value['password']
    };
    console.log(this.data);
    this.service.registerUser(this.data).subscribe(result => {
      console.log(result['message']);
      this.submitUserAlert = result['message'];
      this.userForm.reset();
    }, error => {
      this.errorSubmitAlert = error.error.message[0];
    });
  }

}
