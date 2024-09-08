from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.db import db
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes import api_routes
from flask_migrate import Migrate

db1 = db
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Configuração do CORS
    CORS(app)  # Habilita o CORS para toda a aplicação
    
    db1.init_app(app)

    migrate.init_app(app, db)
    
    # Swagger configuration
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Flask Clean Architecture API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(api_routes)
    return app
