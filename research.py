from main import db, BlogPost, User

a = BlogPost.query.get()
db.session.delete(a)
db.session.commit()