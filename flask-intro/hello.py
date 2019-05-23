# hello.py

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


people = {2:{'fname':'Dima', 'lname':'Marachi','age':24},
          6:{'fname':'Damla', 'lname':'Marasli','age':28},
          10:{'fname':'Linda', 'lname':'Mar','age':20}
         }

@app.route("/")
def hello():
    return "Hello World! <h1> From Dima</h1> <h2> And Damla </h2>"


@app.route("/admin")
def hi():
	return "Hi, From Dima"

@app.route("/admin/")
def bon():
	return "HI, from Dima"
	
@app.route("/admin/<myid>")
def good():
	return "Hi"

@app.route("/admin/<myid>/")
# def admin(myid=None):
#     return "Hello World! - admin v1 - Dima " + str(myid)
def admin(myid = None):
	print('people:', people)
	print('my id is:', int(myid))
	return "Hello World! - admin v1 - Dima Marachi " + \
		str(people.get(int(myid),{'fname':'Who Knows'}))

@app.route("/info")
def info():
    print('Args:', request.args)
    return "Hello World! - from info - Dima - the first parameter parm " + request.args.get('parm1','default1') + " The second parameter lala " + request.args.get('lala','default2')

@app.route("/admin2/<myid>/")
def admin2(myid = None):
	return render_template("person.html", testval="Some Value So We know it works", person=people.get(int(myid),{'fname':'Who Knows'}))

if __name__ == '__main__':
  	app.run(host='0.0.0.0', debug=True)