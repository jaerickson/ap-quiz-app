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
    info = "<h4>"
    if q1 == "correct":
      info += "Question 1: CORRECT</h4><br>"
    else:
      info += "Question 1: INCORRECT</h4><br>"
    if q2 == "correct":
      info += "Question 2: CORRECT</h4><br>"
    else:
      info += "Question 2: INCORRECT</h4><br>"
    if q3 == "correct":
      info += "Question 3: CORRECT</h4><br>"
    else:
      info += "Question 3: INCORRECT</h4><br>"
    if q4 == "correct":
      info += "Question 4: CORRECT</h4><br>"
    else:
      info += "Question 4: INCORRECT</h4><br>"
    if q5 == "correct":
      info += "Question 5: CORRECT</h4><br>"
    else:
      info += "Question 5: INCORRECT</h4><br>"
    if q6 == "correct":
      info += "Question 6: CORRECT</h4><br>"
    else:
      info += "Question 6: INCORRECT</h4><br>"
    return info

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

    
