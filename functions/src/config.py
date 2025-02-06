import firebase_admin
from firebase_admin import credentials, firestore

class Config:
    """Configuraciones generales de la aplicación"""

    # Inicializar Firebase Admin si no está inicializado
    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    # Firestore Database
    db = firestore.client()

    @staticmethod
    def init_app(app):
        """Inicializar configuraciones en la app Flask"""
        app.config["DEBUG"] = True
        app.config["SECRET_KEY"] = "68d57bc53e36c2b0488a8e980b6a07695ac00950fa0b57970305c560f7aa168d"
