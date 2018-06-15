Live Location Tracker
*********************
This is a live location tracker project, taken up during the May 2018 Python Pune Meetup hackathon.
Please look at the comment titled `Live Location and trip tracking through phone app` in the following link:
https://github.com/datameet-pune/datameet-pune.github.io/issues/15


# Installation

### Clone this repo
```
$ git clone git@github.com:screwgoth/live-location-tracker.git
$ cd live-location-tracker
```

## Development Setup for Server

###Pre-requisites
* Python3
* MySQL
* Docker (Optional)

### Create virtual environment (using virtualenvwrapper)
```
$ mkvirtualenv llt
$ workon llt
$ cd server/live-location-tracker
```

### Install Django and other Python requirements
```
(llt)$ pip install -r requirements.txt
```

### Start MySQL Server
You can use any MySQL server. 
In  this example, in order to user a Docker container of MySQL DB, use the following command
```
$ docker run --name llt-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=llt-db -p 3306:3306 -d mysql:latest --default-authentication-plugin=mysql_native_password
```
In any case, please update the `DATABASES` section in the `settings.py` under the `livelocationtracker` folder with appropriate Database name, user, password, host IP and port. The current values are assuming you are using MySQL server using Docker as given above.

### Start Django Server
```
(llt)$ python manage.py makemigrations
(llt)$ python manage.py migrate
(llt)$ python manage.py createsuperuser --username=admin --email=admin@acme.com
(llt)$ python manage.py runserver 0.0.0.0:8000
```
You can also use gunicorn as follows:
```
(llt)$ gunicorn -b :8000 -D livelocationtracker.wsgi
```

You can open your browser to following URLs:
* http://localhost:8000/admin
* http://localhost:8000/api/v1/location

## Development Setup for Server

### Pre-requisites
* NodeJS v8+

### Build AngularJS app
Update the IP Address or hostname of the system on which the Django server is running the files `web-client/src/environments/environment.prod.ts` and `web-client/src/environments/environment.ts`
Usually, for non-production or dev environments, this can be `localhost` or `127.0.0.1`

```
$ cd web-client
$ npm install
$ npm start
```
You can now access the Web frontend at http://localhost:4200
```
$ npm build
```


# Contributing
* If you want to contribute to the project, first start by creating a Issue or choosing one from the existing issue.
* Fork the repo, create a new branch with your fix and send a Pull Request.
* Alternatively, you can mail me at _raseelbhagat [at] gmail [dot] com_ if you want to get involved.
