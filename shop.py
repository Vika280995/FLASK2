from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Item


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
#db = SQLAlchemy(app)

#class Item(db.Model):
    #id = db.Column(db.Integer,primary_key=True)
    #title = db.Column(db.String(100),nullable=False)
    #price = db.Column(db.Integer,nullable=False)
    #description = db.Column(db.Text, nullable=False)
    #picture = 0
    #isactive = db.Column(db.Boolean,default=True)

    #def __repr__(self):
        #return self.title

#db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createdb')
def createdb():
    db.create_all()
    return 'Tables created'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create',methods=['POST','GET'])
def create():
    if request.method=="POST":
        title = request.form['title']
        price = request.form['price']
        description =  request.form['description']

        item = Item(title=title,price=price, description=description)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"

    else:
        return render_template('create.html')

@app.route('/addition')
def addition():
    return render_template('addition.html')

if __name__ == '__main__':
    app.run(debug=True)
