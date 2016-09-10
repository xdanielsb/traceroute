"""
" This script helps to manage all the pages
"""

#Import the framework
from flask import Flask, render_template, request
import os


#Create the app
app = Flask(__name__)

#Add a wrapper for the home page
@app.route('/')
def homepage():
    #request the program for doing the request
    return render_template('index.html')

@app.route('/traceroute/', methods = ['GET','POST'])
def traceroute():
    data = request.form
    #extracting the parameters
    address= data["ip"]
    phantom = "export PATH=$PATH:/opt/phantom/bin/ && "
    casper = "/opt/casperjs/bin/casperjs "
    script = "~/Documents/myProjects/scripting/logic/casper/global-crossing.js "
    arguments = "--addr="+address
    pipe = " | tee "+address+".temp"
    command = phantom + casper + script + arguments + pipe 
    os.system(command)
    #reading the answer
    response = open(address+".temp", "r+").read()    
    return render_template('index.html', response=response)

#Start the app
if __name__=="__main__":
    app.secret_key = '879sd3$55cDS'
    app.run(debug=True)

