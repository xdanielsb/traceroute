"""
" This script helps to manage all the pages
"""

#Import the framework
from flask import Flask, render_template
import subprocess


#Create the app
app = Flask(__name__)

#Add a wrapper for the home page
@app.route('/')
def homepage():
    #request the program for doing the request
    command = "export PATH=$PATH:/opt/phantom/bin/ &&  \
    /opt/casperjs/bin/casperjs \
    ~/Documents/myProjects/scripting/logic/casper/look.js | tee response.temp"
    os.system(command)
    
    return render_template('index.html')

#Start the app
if __name__=="__main__":
    app.secret_key = '879sd3$55cDS'
    app.run(debug=True)

