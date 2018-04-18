from flask import Flask
from flask_mongoengine import MongoEngine
from apps.category.controllers import CategoryView


app = Flask(__name__)

db = MongoEngine()
app.config.from_pyfile('config/settings.py')
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


app.add_url_rule('/categories', view_func=CategoryView.as_view('categories'))
