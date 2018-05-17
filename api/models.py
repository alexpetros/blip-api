
class Post(db.Document):
    caption = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    videoUrl = db.StringField(required=True)
    comments = db.ListField(EmbeddedDocumentField(Comment))
    created = DateTimeField()
    meta = {
        'indexes': [
            '-created' # indexes on most recent post
        ]
    }

class Comment(db.EmbeddedDocument):
    user = db.ReferenceField(User)
    text = db.StringField()

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    full_name = db.StringField(max_length=100)
    posts = db.ListField(ReferenceField(Post))
    meta = {
        'indexes': [
            '$full_name',  # text index for searching users by name
        ]
    }
