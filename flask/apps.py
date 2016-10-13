from flask import Flask, url_for, render_template, request, redirect
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/kloubi.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))

    def __init__(self, username, email, fname, lname):
        self.username = username
        self.email = email
        self.fname = fname
        self.lname = lname

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(fname = request.form['name'], 
                        lname = request.form['surname'],
                        email = request.form['email'],
                        username = request.form['username'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')