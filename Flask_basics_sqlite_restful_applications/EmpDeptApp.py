from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Department(db.Model):
    deptno = db.Column(db.Integer, primary_key = True)
    dName = db.Column(db.String)
    loc = db.Column(db.String)

    def dept_serialize(self):
        return {
            "deptno" : self.deptno,
            "dName" : self.dName,
            "loc" : self.loc
        }
    def __str__(self) -> str:
        return self.deptno + self.dName + self.loc

class Employee(db.Model):
    empid = db.Column(db.Integer, primary_key = True)
    empName =  db.Column(db.String)
    empSal =  db.Column(db.Integer)
    deptno = db.Column(db.Integer)

    def emp_serialize(self):
        return {
            "empid" : self.empid,
            "empName" : self.empName,
            "empSal" : self.empSal,
            "department" :Department.query.get(self.deptno).dept_serialize()
        }
        
    def __str__(self):
        return self.empid + self.empName + self.empSal

@app.route('/create_dept', methods = ['POST'])
def create_department():
    if request.method == 'POST':
        d = request.get_json()

        dept = Department(
            dName = d.get('dName'),
            loc =  d.get('loc')
        )
        db.session.add(dept)
        db.session.commit()
        message = {
            "data" : "Record Inserted Succesfully"
        }
        return jsonify(message)

@app.route('/create_emp', methods = ['POST'])
def create_employee():
    if request.method == 'POST':
        e = request.get_json()

        emp = Employee(
            empName = e.get('empName'),
            empSal = e.get('empSal'),
            deptno = e.get('deptno')
        )
        db.session.add(emp)
        db.session.commit()
        message = {
            "data" : "Record Inserted Succesfully"
        }
        return jsonify(message)


@app.route('/list', methods =[ 'GET'])
def list_department():
    dept = Department.query.all()
    listDept = []
    for d in dept:
        listDept.append(d.dept_serialize())
    return jsonify(listDept)

@app.route('/list_emp', methods =[ 'GET'])
def list_employee():
    emp = Employee.query.all()
    listEmp = []
    for e in emp:
        listEmp.append(e.emp_serialize())
    return jsonify(listEmp)

@app.route('/passId/<int:empId>', methods = ['GET'])
def get_employee_details(empId):
    return Employee.query.get(empId).emp_serialize()


with app.app_context():
    db.create_all()
app.run(debug=True)