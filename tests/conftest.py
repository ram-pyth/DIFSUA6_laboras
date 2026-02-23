import pytest
from app import app, db


@pytest.fixture
def client():
    # Configure app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for easier testing

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()
