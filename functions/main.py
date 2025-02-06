import sys
import os
from firebase_admin import initialize_app
from firebase_functions import https_fn

# Añadir el directorio 'src' al path para que Python pueda encontrarlo
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Imprimir sys.path para verificar si 'src' está en el path
print("SYS_PATH: ", sys.path)

# Ahora, importa desde el directorio correcto
from src.api.main import create_app

# Inicializar Firebase Admin (solo en Firebase Functions)
initialize_app()

# Crear la app Flask
app = create_app()

@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()

# Ejecutar en modo local
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
