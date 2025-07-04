from flask import Flask
from config import Config
from flask_cors import CORS

from extensions import db, migrate, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    # ✅ Habilita CORS globalmente para todas as rotas e métodos
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Carrega configurações da aplicação
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importa modelos
    from models import user, diary

    # Importa e aplica CORS nos blueprints (antes de registrar)
    from routes.auth_routes import auth_bp
    from routes.diary_routes import diary_bp

    CORS(auth_bp, origins="*")      # opcional se CORS(app) já cobre
    CORS(diary_bp, origins="*")     # opcional se CORS(app) já cobre

    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)

    return app
