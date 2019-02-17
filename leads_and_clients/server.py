from flask import Flask, redirect, render_template, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
	mysql = connectToMySQL("mydb")
	my_customers = mysql.query_db("SELECT * FROM customers")
	lnthOfCustomers = len(my_customers)
	print(my_customers)
	return render_template("index.html", customers = my_customers, lnth = lnthOfCustomers)

if __name__ == "__main__":
    app.run(debug=True)