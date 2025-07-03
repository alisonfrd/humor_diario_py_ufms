from flask import Flask
from config import Config
from flask_cors import CORS

from extensions import db, migrate, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

    CORS(app, resources={r"/*": {"origins": origins}}, supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from models import user, diary
