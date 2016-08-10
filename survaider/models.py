from flask import url_for
from survaider import db

class Hotels(db.EmbeddedDocument):
    property_id = db.StringField(max_length=255, required=True)
    name = db.StringField(max_length=255, required=True)

class Relation(db.Document):
    parent = db.EmbeddedDocumentField('Hotels')
    units = db.ListField(db.EmbeddedDocumentField('Hotels'))

class Reviews(db.Document):
    property_id = db.StringField(max_length=255, required=True)
    rating = db.StringField(max_length=10)
    review = db.StringField()
    sentiment = db.StringField(max_length=255)
    review_link = db.StringField()


