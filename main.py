from flask import Flask

from config.settings.base import DATABASE_URL

from controllers.test import test_bp
from utils.db import init_db

from controllers.books_controller import books_bp
from controllers.damage_levels_controller import damage_levels_bp
from controllers.reader_categories_controller import reader_categories_bp
from controllers.rents_controller import rents_bp
from controllers.users_controller import users_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

init_db()
app.register_blueprint(test_bp)
app.register_blueprint(users_bp)
app.register_blueprint(books_bp)
app.register_blueprint(damage_levels_bp)
app.register_blueprint(reader_categories_bp)
app.register_blueprint(rents_bp)

if __name__ == "__main__":
    app.run(debug=True)
