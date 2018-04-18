import os


MONGODB_SETTINGS = {
    'host': os.environ.get('MONGODB_HOST', 'localhost'),
    'port': int(os.environ.get('MONGODB_PORT', 27017)),
    'db': os.environ.get('MONGODB_DB'),
}
