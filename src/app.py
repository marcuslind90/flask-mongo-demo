from flask import Flask
from flask_mongoengine import MongoEngine
from apps.category.views import CategoryView
from apps.api.utils import register_api


app = Flask(__name__)

db = MongoEngine()
app.config.from_pyfile('config/settings.py')
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


register_api(app, CategoryView, 'categories', '/categories/')
