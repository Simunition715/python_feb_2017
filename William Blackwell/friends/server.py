from flask import *
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	data = {
		'friends': users,
	}

	return render_template('index.html', data=data)

@app.route('/users', methods=['POST'])
def create_user():
	query = "INSERT INTO users(name , created_at, updated_at) VALUES (:name, NOW(), NOW())"
	values = {
		'name': request.form['name']
	}
	mysql.query_db(query,values)
	return redirect('/')

@app.route("/friends/<id>/edit")
def edit_user(id):
	query = 'SELECT * FROM users WHERE id = :id'
	values = {
		'id': id
	}
	users = mysql.query_db(query,values)
	data = {
		'users' : users
	}

	return render_template ('edit.html', data=data)

@app.route('/friends/<id>', methods=['POST'])
def update_user(id):
	query = "UPDATE users SET name = :name where id = :id;"
	print "*" * 20
	print id
	print request.form['name']
	values = {
		'name': request.form['name'],
		'id':id
	}
	mysql.query_db(query,values)
	return redirect('/')

@app.route('/friends/<id>/delete')
def destroy_user(id):
	query = "DELETE FROM users WHERE id = :id"
	data = {
		'id': id
	}
	mysql.query_db(query, data)
	return redirect('/')		


# an example of running a query
print mysql.query_db("SELECT * FROM users")

app.run(debug=True)