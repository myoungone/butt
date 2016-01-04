from mongoengine import Document, StringField, EmailField


class Friend(Document):
    name = StringField()
    nickname = StringField()
    category = StringField()
    institute = StringField()
    title = StringField()
    phone = StringField()
    email = EmailField()
    birth = StringField()
    location = StringField()
