from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ecommerce_db'

mysql = MySQL(app)

# Sample route to fetch users
@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
