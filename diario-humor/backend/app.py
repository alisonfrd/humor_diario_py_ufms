from flask import Flask
from config import Config
from flask_cors import CORS

from extensions import db, migrate, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    
    # ✅ Habilita CORS para todas as rotas e origens
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


    # Carrega configurações da aplicação
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importa modelos (para que o Flask-Migrate reconheça)
    from models import user, diary

    # Registra os blueprints
    from routes.auth_routes import auth_bp
    from routes.diary_routes import diary_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)

    return app