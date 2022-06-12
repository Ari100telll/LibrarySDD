from flask import Flask
from flask_cors import CORS

from config.settings.base import DATABASE_URL
from controllers.books_controller import books_bp
from controllers.damage_levels_controller import damage_levels_bp
from controllers.reader_categories_controller import reader_categories_bp
from controllers.rents_controller import rents_bp
from controllers.users_controller import users_bp
from resources import db, ma
from startup_script import run_startup_script

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

app.register_blueprint(users_bp)
app.register_blueprint(books_bp)
app.register_blueprint(damage_levels_bp)
app.register_blueprint(reader_categories_bp)
app.register_blueprint(rents_bp)

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()
    run_startup_script()

if __name__ == "__main__":
    app.run(debug=True)
