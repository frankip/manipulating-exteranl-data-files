import sqlite3
from flask import Flask, jsonify, render_template
from files import Employee, fetch_data_from_sql, load_data_from_csv_file


app = Flask(__name__)

def get_db_connection():
    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        return conn

@app.route("/")
def load_data_file_contents():
    name = "Francis"
    # load_data_from_csv_file()
    conn = get_db_connection()
    # post  = fetch_data_from_sql()
    # all  = fetch_data_from_sql()

    all = Employee.fetch_data()
    # all = jsonify(user.to_json for user in all_emp)
    # print(post)

    return render_template('index.html', name=name, all=all )

@app.route("/add")
def create_new_employee():
    new_emp = Employee('2','http://dummyimage.com/208x100.png/cc0000/ffffff','Francis','KIPu','kiping@onehundre.com','Training','13')
    new_emp.add_new(new_emp)

    return load_data_file_contents()

@app.route("/update")
def update_new_employee():

    # Employee.update('iitschakov0@soup.io')
    # new_emp = Employee('2','http://dummyimage.com/208x100.png/cc0000/ffffff','Francis','KIP','kiping@onehundre.com','Training','13')
    # new_emp.add_new(new_emp)

    return Employee.update('iitschakov0@soup.io')

@app.route("/delete")
def delete_new_employee():

    # Employee.update('iitschakov0@soup.io')
    # new_emp = Employee('2','http://dummyimage.com/208x100.png/cc0000/ffffff','Francis','KIP','kiping@onehundre.com','Training','13')
    # new_emp.add_new(new_emp)

    usr = Employee.delete_employee('iitschakov0@soup.io')
    return f"employee {usr} has been deleted"