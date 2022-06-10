from flask import Flask

from config.settings.base import DATABASE_URL
from controllers.test import test_bp
from utils.db import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

app.register_blueprint(test_bp)
init_db()

if __name__ == "__main__":
    app.run(debug=True)
