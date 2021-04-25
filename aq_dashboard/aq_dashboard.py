"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask

def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        """Base view."""
        return 'TODO - part 2 and beyond!'

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8888)
