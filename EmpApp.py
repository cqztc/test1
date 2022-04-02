from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    choice_attendance = request.form['attendance']
    date_and_time = request.form['Date_Time']
   # last_name = request.form['last_name']
  #  pri_skill = request.form['pri_skill']
  #  location = request.form['location']
   # emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s)"
    

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=first_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
