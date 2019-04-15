# menusection-rest-api

## Install guide

#### 1. Clone the repo
```bash
$ git clone git@github.com:LiamWahahaha/menusection-rest-api.git
$ cd menusection-rest-api
```

#### 2. Create the virtualenv
```bash
$ python3 -m venv venv
```

#### 3. Install dependencies
```bash
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

#### 4. Run the app
```bash
$ python3 app.py
$ python3 app.py --host 0.0.0.0
$ python3 app.py --host 127.0.0.1 --port 5001
```
default host is 127.0.0.1

default port is 5000

## API documentation

* GET ```/menusection```

  Get all menu sections

* GET ```/menusection/<int:id>```

  Get a menu section by id

* POST ```/menusection```

  Add a new menu section

* POST ```/menusection/<int:id>```

  Edit a menu section

* DELETE ```/menusection/<int:id>```

  Delete a menu section

## Using curl to test the API

* Get all menu sections

  ```curl -v http://host:port/menusection```

* Get a menu section by id

  ```curl -v http://host:port/menusection/<id>```

* Add a new menu section

  ```curl http://host:port/menusection -d 'name=Lunch Specials' -X POST```

* Edit a menu section

  ```curl http://host:port/menusection/<id> -d 'name=Lunch Special' -X POST```

* Delete a menu section

  ```curl http://host:port/menusection/<id> -X DELETE```

