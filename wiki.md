# Scrub My List Development Process


## Step 1: Planning
-Defined the requirements and wrote the key user stories  
-Used a mockup tool (cacoo.com) to create a mockup of the web app.    
-Decided on structuring the pages to have a body made of 3 parts: a header with a navbar, a main section and a footer. The header and footer stay the same across all the webpages, so will be defined in base.html. All the child templates will inherit the structure and styling of the header and footer from base.html. The contents and styling of the main section will change from one page to another, so will be defined in each child template.    
-Gathered all required images (Favicon and Home page image) and saved them in the static/img directory of the project  
-Identified all the templates needed  
    -index.html (the home page)   
    -upload_list.html (form for uploading email list)  
    -view_lists.html (table showing details of email lists uploaded)  
    -register.html (sign up form)  
    -login.html (login page)  
    -profile.html (page will show user session details) 
    -base.html (parent template that will define the structure and styling of the web app)  


## Step 2: Project Setup 
-Decided to use blueprints right away as I find it simpler than to start with a single module then copy and paste code into different scripts.  

### 2.1 Virtual Environment
```
$mkdir "Scrub My List"
$python -m venv env
$env/Scripts/activate
$pip install flask
$pip install pytest
$pip install flask-sqlalchemy
$pip install flask-migrate
$pip install flask-login
$pip freeze > requirements.txt
```

### 2.2 Project Directory Structure
``` 
|- app.py
|- config.py
|- requirements.txt
|- readme.md
|- wiki.md
|- .gitignore
|- env/
|- instance/
|- project
    |- __init__.py
    |- emails.py
    |- models.py
    |- auth
    |- emails
    |- templates
        |- base.html
        |- auth
            |- login.html
            |- profile.html
            |- register.html
        |- emails
            |- index.html
            |- list_upload.html
            |- view_lists.html
    |- static
        |- css/
        |- img/
|- tests
    |- __init__.py
    |- conftest.py
    |- test_functionality.py
    |- test_app.py
    |- test_models.py
```

### 2.3 config.py
-Set up application configurations in config.py  
-Included 2 configuration settings to secure file uploads:  
-Used a configuration option provided by flask to limit the size of files users can upload. The `MAX_CONTENT_LENGTH` option controls the maximum size a request body can have. If a POST request body exceeds 1MB flask will discard the request with a 413 status code.  
-Used the `UPLOAD_EXTENSIONS` to specify the acceptable types of files a user can upload (only text and csv allowed). If a user tries to upload a file whose extension is not in the allowed list, flask will reject the POST request with a 400 status code.  

### 2.4 project/init.py
-Defined the flask application factory function  
-Configured the flask app  
-Configured logging  
-Registered blueprints, reqest callback functions and custom error pages.  
-Initialized all flask extensions (sqlalchemy, migrations)

### 2.5 Created the blueprints in the init.py files and defined the views in the views.py files
-No code for the views or templates was written, just defining them so they exist.  
-Example below is shown for auth blueprint but the same thing was done for the emails blueprint  

**Auth blueprint init.py file:**
```
"""
The auth blueprint handles everything related to user management- user registration, user login, user logout, user profile for changing credentials

"""

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

from . import views

```

**Auth blueprint views.py file**
```
from . import auth_blueprint
from flask import render_template

@auth_blueprint.route('/register')
def register():
    return render_template('auth/register.html')

@auth_blueprint.route('/login')
def login():
    return render_template('auth/login.html')


@auth_blueprint.route('/profile')
def profile():
    return render_template('auth/profile.html')
```

**Example of what the templates contain (register.html)**
```
<h1>This will be a registration page</h1>
```

**Emails blueprint views.py file**
```
from . import emails_blueprint
from flask import render_template


@emails_blueprint.route('/')
def index():
    return render_template('emails/index.html')


@emails_blueprint.route('/view_lists/')
def view_lists():
    return render_template('emails/view_lists.html')


@emails_blueprint.route('/upload_list')
def upload_list():
    return render_template('emails/upload_list.html')

```

### 2.6 Instantiated the flask app in app.py and tested that all the routes were setup correctly.  
```
from project import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

## Step 3: Code for base.html and CSS Styling
-Make all templates inherit structure and styling from base.html   

## Step 4: 