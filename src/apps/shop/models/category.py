from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Category(Document):
    name = StringField(required=True, max_length=200)
    slug = StringField(required=True, unique=True)
    created_at = DateTimeField(default=datetime.utcnow)
