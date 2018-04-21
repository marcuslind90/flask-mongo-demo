from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime


class Product(Document):
    name = StringField(required=True, max_length=200)
    slug = StringField(required=True, unique=True)
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
