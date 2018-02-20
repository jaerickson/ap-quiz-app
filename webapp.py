import os
import json
from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)


# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars). 
  
  
  
def get_info(q1, q2, q3, q4, q5, q6):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    if q1 == "correct":
      one = "Question 1: CORRECT"
    else:
      one = "Question 1: INCORRECT"
    if q2 == "correct":
      two = "Question 2: CORRECT"
    else:
      two = "Question 2: INCORRECT"
    if q3 == "correct":
      three = "Question 3: CORRECT"
    else:
      three = "Question 3: INCORRECT"
    if q4 == "correct":
      four = "Question 4: CORRECT"
    else:
      four = "Question 4: INCORRECT"
    if q5 == "correct":
      five = "Question 5: CORRECT"
    else:
      five = "Question 5: INCORRECT"
    if q6 == "correct":
      six = "Question 6: CORRECT"
    else:
      six = "Question 6: INCORRECT"
    return Markup("<h4>" + one + "</h4><br><h4>" + two + "</h4><br><h4>" + three + "</h4><br><h4>" + four + "</h4><br><h4>" + five + "</h4><br><h4>" + six + "</h4>") 

@app.route('/')
def render_main():
        return render_template('home.html')
    
@app.route('/lang', methods=['GET','POST'])
def render_lang():
  if 'q1' in request.form:
        return render_template('lang.html', info = get_info(request.form['q1'], request.form['q2'], request.form['q3'], request.form['q4'], request.form['q5'], request.form['q6']))
  else:
    return render_template('lang.html')
@app.route('/chem', methods=['GET','POST'])
def render_chem():

        return render_template('chem.html')

@app.route('/startOver')
def startOver():
    session.clear() #clear variable values and create a new session
    return redirect(url_for('render_main'))
  
if __name__=="__main__":
    app.run(debug=False)

    
