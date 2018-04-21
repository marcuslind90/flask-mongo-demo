class ApiException(Exception):
    status_code = 400

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
