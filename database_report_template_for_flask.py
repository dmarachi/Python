# database_report_template_for_flask.py
import database_report
import json
from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/invoice/")
def invoice():
	with open("invoice.txt", "r") as f:
		InvoiceContent = f.read()
	return render_template("invoice.html", InvoiceContent = InvoiceContent)

if __name__ == "__main__":
 	app.run(host= "0.0.0.0", debug=True)