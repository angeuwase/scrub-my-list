# Scrub My List Development Process

# Stage 1: Prep Work
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

# Stage 2: Test-Driven Development - Home Page
-Wrote the code for each view function and its associated template using TDD.
-The unit tests were defined in test_app.py.  
-Example for the TDD process I followed is shown here:

## Step 1: Wrote the test
```
def test_index_page():
    """
    GIVEN a flask web application
    WHEN a GET request for '/' is recieved
    THEN render the home page. There should be a heading and two paragraph text visible

    """

    #mock data
    heading = b'Scrub My List'
    paragraph1 = b'Bulk validate your mailing list and recieve actionable insight regarding its health all in one place!'
    paragraph2a = b'Register' 
    paragraph2b = b'for an account now and begin to enjoy never having to worry about poor bounce rates again!'  

    #the test

    with app.test_client() as client:
        response = client.get('/')

        assert response.status_code == 200
        assert heading in response.data
        assert paragraph1 in response.data
        assert paragraph2a in response.data
        assert paragraph2b in response.data
```

## Result: it failed
-The test failed because the template only contains `<h1>This will be the home page</h1> `
```
FAILED tests/test_app.py::test_index_page - assert b'Bulk validate your mailing list and recieve actionable insight regarding its health all in one place!' in b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content=...
============================================================================================================================ 1 failed in 2.07s ============================================================================================================================= 

```

## Step 2: Wrote the code to pass the test
-Added the required code in the template. The view function was correctly rendering the template so it didnt need to be changed.  
```
tests\test_app.py .                                                                                                                                                                                                                                                   [100%] 

============================================================================================================================ 1 passed in 1.44s ============================================================================================================================= 
```

## Step 3: Refractored the test function so that it uses pytest fixture for test_client
-Defined the pytest fixture for test_client in conftest.py  
-Updated the test function so that it uses the test_client fixture  
(it is going to be repeated a lot, so might as well set it up)

**New test function:**
```
#from app import app                #no longer needed as code is using test_client fixture defined in conftest.py

def test_index_page(test_client):
    """
    GIVEN a flask web application
    WHEN a GET request for '/' is recieved
    THEN render the home page. There should be a heading and two paragraph text visible

    """

    #mock data
    heading = b'Scrub My List'
    paragraph1 = b'Bulk validate your mailing list and recieve actionable insight regarding its health all in one place!'
    paragraph2a = b'Register' 
    paragraph2b = b'for an account now and begin to enjoy never having to worry about poor bounce rates again!'  

    #the test

    response = test_client.get('/')

    assert response.status_code == 200
    assert heading in response.data
    assert paragraph1 in response.data
    assert paragraph2a in response.data
    assert paragraph2b in response.data

```

**New conftest.py file:**
```
import pytest
from project import create_app

@pytest.fixture(scope='module')
def test_client():
    """
    Instantiates a flask application configured for testing, and then
    -creates a test_client for it
    """

    #Creates an instance of the flask app and configures it for testing
    test_app = create_app()
    test_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    testing_client = test_app.test_client()

    return testing_client

```

**Test still passed:**
```
tests\test_app.py .                                                                                                                                                                                                                                                   [100%] 

============================================================================================================================ 1 passed in 0.16s ============================================================================================================================= 

```

# Stage 3: Test-Driven Development- User Model
-Wrote the code for the view functions related to users and their associated templates using TDD.  
-Tests covered:  
*registration
*password hashing
*adding new user to database
*login and logout. 


## Step 1: Write the test for registration
-



# Stage 4: Test-Driven Development- Emails Model
-Wrote the code for the view functions related to emails and their associated templates using TDD.  
-The tests covered:  
*uploading a new email list  
*viewing email lists  
*