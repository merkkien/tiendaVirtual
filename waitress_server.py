import os
from waitress import serve
import app
port = int(os.environ.get('PORT', 33507))
serve(app.app, port=port)