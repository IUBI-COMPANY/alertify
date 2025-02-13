import sys
import os
from firebase_admin import initialize_app
from firebase_functions import https_fn
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.api.main import create_app

load_dotenv()
initialize_app()

app = create_app()

@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()

# run local mode
if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "development":
        app.run(host="127.0.0.1", port=5000, debug=True)
