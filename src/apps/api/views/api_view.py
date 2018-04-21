from flask import request, jsonify
from flask.views import MethodView


class ApiView(MethodView):

    id_field = 'id'
    model = None

    def post(self):
        instance = self.model(**request.form.to_dict()).save()
        response = jsonify(instance)
        response.status_code = 201
        return response

    def get(self, id=None):
        if id is not None:
            instance = self.model.objects(**{self.id_field: id}).first()
            return jsonify(instance)
        else:
            instances = self.model.objects.all()
            return jsonify(instances)

    def put(self, id):
        instance = self.model.objects(**{self.id_field: id}).first()
        instance.modify(**request.form.to_dict())
        return jsonify(instance)

    def delete(self, id):
        instance = self.model.objects(**{self.id_field: id}).first()
        instance.delete()

        response = jsonify()
        response.status_code = 204
        return response

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        # If the request method is HEAD and we don't have a handler for it
        # retry with GET.
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        try:
            return meth(*args, **kwargs)
        except Exception as e:
            response = jsonify({'message': str(e)})
            response.status_code = 400
            return response
