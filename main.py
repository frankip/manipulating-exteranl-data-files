import sqlite3
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from files import Employee, fetch_data_from_sql, load_data_from_csv_file


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        return conn

@app.route("/")
def load_data_file_contents():
    name = "Francis"
    all = Employee.fetch_data()
    # all = jsonify(user.to_json for user in all_emp)
    # print(post)

    return render_template('index.html', name=name, all=all )

@app.route("/add/", methods=('GET', 'POST'))
def create_new_employee():
    if request.method == 'POST':
        image = request.form['image']
        name = request.form['name']
        email = request.form['email']
        # department = request.form['department'].value()
        department = "sales"

        print("-----", department)

        if not name:
            flash('Title is required!')
        elif not email:
            flash('email is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO employees (image, name, email, department) VALUES (?, ?,?,?)',
                         (image, name, email, department))
            print(conn)
            conn.commit()
            conn.close()
            return redirect(url_for('load_data_file_contents'))

    # new_emp = Employee('2','http://dummyimage.com/208x100.png/cc0000/ffffff','Francis','KIPu','kiping@onehundre.com','Training','13')
    # new_emp.add_new(new_emp)

    return render_template('index.html')

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