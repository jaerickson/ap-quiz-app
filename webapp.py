import os
import json
from flask import Flask, url_for, render_template, request, redirect, session, Markup, flash

app = Flask(__name__)


# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars). 
highscore = 0
  
  
def get_info(q1, q2, q3, q4, q5, q6):
    info = ""
    num = 0
    session["sessionhighestnum"] = 0
    if q1 == "correct":
      info += "Question 1: CORRECT, "
      num += 1
    else:
      info += "Question 1: INCORRECT, "
    if q2 == "correct":
      info += "Question 2: CORRECT, "
      num += 1
    else:
      info += "Question 2: INCORRECT, "
    if q3 == "correct":
      info += "Question 3: CORRECT, "
      num += 1
    else:
      info += "Question 3: INCORRECT, "
    if q4 == "correct":
      info += "Question 4: CORRECT, "
      num += 1
    else:
      info += "Question 4: INCORRECT, "
    if q5 == "correct":
      info += "Question 5: CORRECT, "
      num += 1
    else:
      info += "Question 5: INCORRECT, "
    if q6 == "correct":
      info += "Question 6: CORRECT"
      num += 1
    else:
      info += "Question 6: INCORRECT"
    global highscore
    if num >= highscore:
        highscore = num
    session["highScore"] = highscore
    session["numCorrect"] = num
    return Markup("<h4>" + info + "</h4>") 

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
    return redirect(url_for('render_lang'))
  
if __name__=="__main__":
    app.run(debug=False)

    
