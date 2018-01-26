from flask import Flask, request, Markup, render_template, flash
import json
import os

app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')
    
@app.route("/lang")
def render_lang():
        return render_template('lang.html')

@app.route("/chem")
def render_chem():
        return render_template('chem.html')

if __name__=="__main__":
    app.run(debug=False)

    
