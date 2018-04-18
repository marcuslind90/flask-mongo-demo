from flask import jsonify
from flask.views import MethodView
from apps.category.models import Category


class CategoryView(MethodView):

    def get(self):
        categories = Category.objects.all()
        return jsonify(categories.to_json())
