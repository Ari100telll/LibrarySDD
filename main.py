from flask import Flask

from config.settings.base import DATABASE_URL
from urls import load_endpoints
from utils.flask_wrapper import FlaskAppWrapper

flask_app = Flask(__name__)

app = FlaskAppWrapper(flask_app, SQLALCHEMY_DATABASE_URI=DATABASE_URL)

load_endpoints(app)

if __name__ == "__main__":
    app.run(debug=True)
