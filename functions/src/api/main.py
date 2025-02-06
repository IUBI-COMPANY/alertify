from flask import Flask
from src.api.routes import register_routes

app = Flask(__name__)

# Registrar rutas
register_routes(app)

def create_app():
    return app
