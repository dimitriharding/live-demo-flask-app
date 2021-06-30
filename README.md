### Step 1 - Create a virtual environment with
`virtualenv .env`

### Step 2: Activate Virtual Environment
`.env/bin/activate`

### Step 3: Install flask in 
`pip install flask`

### Step 4: Create a flask app file
- Create a file `app/app.py` 
- Paste code from [Flask Quickstart/](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

### Step 5: Run Flask application
- Go to application folder `cd app`
- Run `flask run` to start flask app
- Navigate to http://127.0.0.1:5000/ 

----
Additional Info

`pip freeze` - to see dependencies

----
Uploading to Heruko

