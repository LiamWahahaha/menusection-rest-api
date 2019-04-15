# menusection-rest-api

## Install guide

#### Clone the repo
```bash
$ git clone git@github.com:LiamWahahaha/menusection-rest-api.git
$ cd menusection-rest-api
```

#### Create the virtualenv
```bash
$ python3 -m venv venv
```

#### Install dependencies
```bash
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

#### Run the app
```bash
$ python3 app.py
$ python3 app.py --host 0.0.0.0
$ python3 app.py --host 127.0.0.1 --port 5001
```
default host is 127.0.0.1
default port is 5000
