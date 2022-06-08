from flask import Flask

from config.settings.base import DATABASE_URL
from controllers.books_controller import books_bp
from controllers.test import test_bp
from controllers.users_controller import users_bp

app = Flask(__name__)
app.config(SQLALCHEMY_DATABASE_URI=DATABASE_URL)

app.register_blueprint(test_bp)
app.register_blueprint(users_bp)
app.register_blueprint(books_bp)

if __name__ == "__main__":
    app.run(debug=True)
