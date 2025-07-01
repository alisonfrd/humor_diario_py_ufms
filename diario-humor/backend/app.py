from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from models import user, diary
    from routes.auth_routes import auth_bp
    from routes.diary_routes import diary_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)

    return app
