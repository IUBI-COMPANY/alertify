import firebase_admin
from firebase_admin import credentials, firestore

class Config:
    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    firestore = firestore.client()

    @staticmethod
    def init_app(app):
        """initialize configs app Flask"""
        app.config["DEBUG"] = True
        app.config["SECRET_KEY"] = "68d57bc53e36c2b0488a8e980b6a07695ac00950fa0b57970305c560f7aa168d"
