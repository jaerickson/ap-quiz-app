import os
import json
from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars). 
  
@app.route('/')
def render_main():
        return render_template('home.html')
    
@app.route('/lang', methods=['GET','POST'])
def render_lang():
      with open('values.json') as values_data:
        values = json.load(values_data)
        return render_template('lang.html', val1 = values[0][0]["Value One"], val2 = values[0][0]["Value Two"], val3 = values[0][0]["Value Three"], val4 = values[0][0]["Value Four"])

@app.route('/chem', methods=['GET','POST'])
def render_chem():
      with open('values.json') as values_data:
        values = json.load(values_data)
        return render_template('chem.html', val1 = values[1][0]["Value One"], val2 = values[1][0]["Value Two"], val3 = values[1][0]["Value Three"], val4 = values[1][0]["Value Four"])

@app.route('/startOver')
def startOver():
    session.clear() #clear variable values and create a new session
    return redirect(url_for('render_main'))
  
if __name__=="__main__":
    app.run(debug=False)

    
