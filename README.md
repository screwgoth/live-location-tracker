Live Location Tracker
*********************
This is a live location tracker project, taken up during the May 2018 Python Pune Meetup hackathon.
Please look at the comment titled `Live Location and trip tracking through phone app` in the following link:
https://github.com/datameet-pune/datameet-pune.github.io/issues/15


# Development Setup

### Clone this repo
```
$ git clone git@github.com:screwgoth/live-location-tracker.git
$ cd live-location-tracker
```

### Create virtual environment (using virtualenvwrapper)
```
$ mkvirtualenv llt
$ workon llt
```

### Install Django and other Python requirements
```
(llt)$ pip install -r requirements.txt
```

### Start MySQL Server
You can use any MySQL server. In order to user a Docker container of MySQL DB, use the following command
```
$ docker run --name llt-db -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=llt-db -p 3306:3306 -d mysql:latest --default-authentication-plugin=mysql_native_password
```
In any case, please update the `DATABASES` section in the `settings.py` under the `livelocationtracker` folder with appropriate Database name, user, password, host IP and port. The current values are assuming you are using MySQL server using Docker as given above.

### Start Django Server
```
(llt)$ python manage.py makemigrations
(llt)$ python manage.py migrate
(llt)$ python manage.py createsuperuser --username=admin --email=admin@acme.com
(llt)$ python manage.py runserver 0.0.0.0:8000
```
You can open your browser to following URLs:
* http://localhost:8000/admin
* http://localhost:8000/api/v1/location

# Contributing
* If you want to contribute to the project, first start by creating a Issue or choosing one from the existing issue.
* Fork the repo, create a new branch with your fix and send a Pull Request.
* Alternatively, you can mail me at _raseelbhagat [at] gmail [dot] com_ if you want to get involved.
