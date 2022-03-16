import sqlite3
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from files import Employee, fetch_data_from_sql, load_data_from_csv_file

from init_db import create_data_base_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# instantiate db connetion and tables
create_data_base_connection()


def get_db_connection():
    """ create a connection with the database to write or add files"""
    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        return conn


@app.route("/", methods=('GET', 'POST'))
def load_data_file_contents():
    if request.method == 'POST':
        image = request.form['image']
        name = request.form['name']
       
        email = request.form['email']
        # department = request.form['department'].value()
        department = "sales"

        if not name:
            flash('First name is required!')

        elif not email:
            flash('email is required!')
        else:
            first_name, last_name = name.split()
            conn = get_db_connection()
            conn.execute('INSERT INTO MOCK_DATA(image, first_name, last_name, email, department) VALUES (?, ?, ?,?,?)',
                         (image, first_name, last_name, email, department))
            conn.commit()
            conn.close()
            return redirect(url_for('load_data_file_contents'))

    name = "Francis"
    all = Employee.fetch_data_from_sql()

    return render_template('index.html', name=name, all=all )

@app.route("/add/", methods=('GET', 'POST'))
def create_new_employee():
    if request.method == 'POST':
        image = request.form['image']
        name = request.form['name']
        email = request.form['email']
        departments = request.form['department'].value()
        department = "sales"

        if not name:
            flash('Title is required!')
        elif not email:
            flash('email is required!')
        else:
            # conn = get_db_connection()
            # conn.execute('INSERT INTO employees (image, name, email, department) VALUES (?, ?,?,?)',
            #              (image, name, email, department))
            # print(conn)
            # conn.commit()
            # conn.close()
            return redirect(url_for('create_new_employee'))

    return render_template('index.html')

@app.route("/update")
def update_new_employee():

    # Employee.update('iitschakov0@soup.io')
    return Employee.update('iitschakov0@soup.io')

@app.route("/delete")
def delete_new_employee():

    usr = Employee.delete_employee('iitschakov0@soup.io')
    return f"employee {usr} has been deleted"