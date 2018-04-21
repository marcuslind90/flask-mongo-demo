from flask import Flask
from flask_mongoengine import MongoEngine
from apps.shop import views
from apps.api.utils import register_api


app = Flask(__name__)

db = MongoEngine()
app.config.from_pyfile('config/settings.py')
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


register_api(app, views.CategoryView, 'categories', '/categories/')
register_api(app, views.ProductView, 'products', '/products/')
register_api(app, views.ManufacturerView, 'manufacturers', '/manufacturers/')
