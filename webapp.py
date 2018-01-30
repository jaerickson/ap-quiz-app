import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars). 

def get_questions():

@app.route('/')
def render_main():
        return render_template('home.html')
    
@app.route('/lang',methods=['GET','POST'])
def render_lang():
        return render_template('lang.html')

@app.route('/chem',methods=['GET','POST'])
def render_chem():
        return render_template('chem.html')

@app.route('/startOver')
def startOver():
    #clear variable values and create a new session
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

if __name__=="__main__":
    app.run(debug=False)

    
