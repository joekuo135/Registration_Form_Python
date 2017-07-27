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
    print(request.form)
    today = date.today()
    session['email'] = request.form['email']
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['dob'] = request.form['dob']
    session['password'] = request.form['password']
    session['confirmpw'] = request.form['confirmation']
    print('assigned session variables')

    flag = False
# email info
    if len(request.form['email']) < 1:
        flag = True
        flash("*All fields are required and must not be blank!!")       
    if not EMAIL_REGEX.match(request.form['email']):
        flag = True
        flash("*Invalid email address!!")
    
# name info
    if len(request.form['firstname'])<1:
        flag = True
        flash("*All fields are required and must not be blank!!")    
    elif not NAME_REGEX.match(request.form['firstname']):
        flag = True
        flash("*Invalid First name!!")
    elif len(request.form['lastname'])<1:
        flag = True
        flash("*All fields are required and must not be blank!!")   
    elif not NAME_REGEX.match(request.form['lastname']):
        flag = True
        flash("*Invalid Last name!!")     
# dob info
    elif len(request.form['dob']) < 1:
        flag = True
        flash("*Must provide date of birth!!")       

# password info
    if len(request.form['password'])<8:
        session.pop('password')
        session.pop('confirmpw')
        flag = True
        flash("*Password should be at least 8 characters")   
    elif not PW_REGEX.match(request.form['password']):
        session.pop('password')
        session.pop('confirmpw')
        flag = True
        flash("*Password needs at least 1 Capital 1 Lowercase and 1 special character!!")
    elif request.form['password'] != request.form['confirmation']:
        session.pop('password')
        session.pop('confirmpw')
        flag = True
        flash("*Password do not match!!")
    print('did if and elif')
    if flag == True:
        return redirect('/')
    else:
        return render_template('result.html')


@app.route('/reset', methods=['POST', 'GET'])
def reset():
    session.pop('email', None)
    session.pop('firstname', None)
    session.pop('lastname', None)
    session.pop('dob', None)
    session.pop('password', None)
    session.pop('confirmpw', None)
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)


    # if len(request.form['password']) > 0 :
    #     if len(request.form['password']) < 8:
    #         session.pop('password', None)
    #         session.pop('confirmpw',None)
    #         flag = True
    #         flash("Password must be at least 8 characters")
    #     if not PW_REGEX.match(request.form['password']):
    #         session.pop('psw', None)
    #         session.pop('confirmpw',None)
    #         flag = True
    #         flash("Password needs at least 1 Capital 1 Lowercase and 1 special character!!")
    #     if not request.form['password'] == request.form['confirmation']:
    #         session.pop('password', None)
    #         session.pop('confirmpw',None)
    #         flag = True
    #         flash("Password do not match!!")


    #  if len(request.form['password'])>0:
    #     if len(request.form['password'])<8:
    #         session.pop('password')
    #         session.pop('confirmpw')
    #         flag = True
    #         flash("Password must be at least 8 characters")   
    #     elif not PW_REGEX.match(request.form['password']):
    #         session.pop('password')
    #         session.pop('confirmpw')
    #         flag = True
    #         flash("Password needs at least 1 Capital 1 Lowercase and 1 special character!!")
    #     elif request.form['password'] != request.form['confirmation']:
    #         session.pop('password')
    #         session.pop('confirmpw')
    #         flag = True
    #         flash("Password do not match!!")

