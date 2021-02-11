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

def test_profile_page(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass