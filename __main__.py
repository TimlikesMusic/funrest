import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from app import get_app 

app = get_app()
app.run(debug=False, port=8080)