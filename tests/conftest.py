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