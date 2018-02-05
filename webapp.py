import os
import json
from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars). 

 with open('values.json') as values_data:
        valuess = json.load(values_data)
  
def get_lang_questions(number):
values = {}
values[q1][val1] = 
values[q1][val2] = 
values[q1][val3] = 
values[q1][val4] = 
values[q2][val1] = 
  
def get_chem_questions(number):
  
@app.route('/')
def render_main():
        return render_template('home.html')
    
@app.route('/lang', methods=['GET','POST'])
def render_lang():
        return render_template('lang.html', val1 = Markup(str(<p>C<sub>2</sub></p>)), val2 = 12, val3 = 14, val4 = 16)

@app.route('/chem', methods=['GET','POST'])
def render_chem():
        return render_template('chem.html', val1 = 5, val2 = 6, val3 = 7, val4 = 8)

@app.route('/startOver')
def startOver():
    session.clear() #clear variable values and create a new session
    return redirect(url_for('render_main'))
  
 
  
if __name__=="__main__":
    app.run(debug=False)

    
