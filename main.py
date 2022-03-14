from flask import Flask, jsonify, render_template
from files import Employee, load_data_from_csv_file
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Francis"
    # load_data_from_csv_file()
    all = Employee.fetch_data()
    # all = jsonify(user.to_json for user in all_emp)
    # print(all_emp)

    return render_template('index.html', name=name, all=all )