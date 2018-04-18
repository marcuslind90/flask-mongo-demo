from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Category(Document):
    title = StringField(required=True, max_length=200)
    created_at = DateTimeField(default=datetime.utcnow)
