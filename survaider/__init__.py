from flask import Flask
import warnings
from flask.exthook import ExtDeprecationWarning

warnings.simplefilter('ignore', ExtDeprecationWarning)
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "survaider_task"}
app.config["SECRET_KEY"] = "h89ddjhfS3cr3t078s85"

CORS(app)

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from survaider.views import api
    app.register_blueprint(api)

register_blueprints(app)

if __name__ == '__main__':
    app.run()