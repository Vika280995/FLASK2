from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text, nullable=False)
    #picture = 0
    isactive = db.Column(db.Boolean,default=True)

    def __repr__(self):
        return self.title
