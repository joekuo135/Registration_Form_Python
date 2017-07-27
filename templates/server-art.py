from flask import Flask, render_template, request, redirect, session, flash
from datetime import date, datetime, timedelta
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z\-]+$')
PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z]).+$')
app = Flask(__name__)
app.secret_key = 'myKey'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    today = date.today()
    session['email'] = request.form['email']
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['dob'] = request.form['dob']
    session['password'] = request.form['password']
    session['confirmpw'] = request.form['confirmation']


    errors=[]
# check email
    if len(request.form['email']) < 1:
        errors.append("All fields are required and must not be blank!!")    
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid email address!!")
   
# check first name
    if len(request.form['firstname'])<1:
        errors.append("All fields are required and must not be blank!!") 
    elif not NAME_REGEX.match(request.form['firstname']):
        errors.append("Invalid First name!!")

# check last name      
    if len(request.form['lasttname'])<1:
        errors.append("All fields are required and must not be blank!!")
    elif not NAME_REGEX.match(request.form['lastname']):
        errors.append("Invalid Last name!!")     

# password info
    if len(request.form['password'])<8:
        session.pop('password')
        session.pop('confirmpw')
        errors.append("Password should be at least 8 characters")   
    elif not PW_REGEX.match(request.form['password']):
        session.pop('password')
        session.pop('confirmpw')
        errors.append("Password needs at least 1 Capital 1 Lowercase and 1 special character!!")
    elif request.form['password'] != request.form['confirmation']:
        session.pop('password')
        session.pop('confirmpw')
        errors.append("Password do not match!!")
   
    if len(errors)>0:
        for error in errors:
            flash(error, 'errors')
        return redirect('/')

    else:
        return render_template('result.html')


@app.route('/reset', methods=['POST', 'GET'])
def reset():
    session.pop('email')
    session.pop('firstname')
    session.pop('lastname')
    session.pop('dob')
    session.pop('password')
    session.pop('confirmpw')
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)
