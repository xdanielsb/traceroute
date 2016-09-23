"""
" This script helps to manage all the pages
"""

#Import the framework
from __future__ import print_function
from flask import Flask, render_template, request
import os
from process_file import get_parameters 

#Create the app
app = Flask(__name__)

#Add a wrapper for the home page
@app.route('/')
def homepage():
    #request the program for doing the request
    return render_template('index.html')

@app.route('/graph/')
def graph():

    targetip, ttlip, route = get_parameters()
    print(targetip, ttlip, route )
    num_links = len(route)

    #request the program for doing the request
    return render_template('graph2.html', targetip=targetip, ttlip= ttlip, route=route, num_links = num_links)

@app.route('/traceroute/', methods = ['GET','POST'])
def traceroute():
    data = request.form
    #extracting the parameters
    address= data["ip"]
    source = data["source"]
    
    print(data)
    phantom = "export PATH=$PATH:/opt/phantom/bin/ &&  "
    casper = "/opt/casperjs/bin/casperjs "

    script = "~/Documents/myProjects/scripting/logic/casper/eastlink.js "
    argumentip = "--addr="+address
    argumentsource = " --source='"+source+"'"
    pipe = " | tee "+address+".temp"
    command = phantom + casper + script + argumentip + argumentsource + pipe 
    
    
    print (command)
    #execute the command
    os.system(command)
    #reading the answer
    response = open(address+".temp", "r+").read() 
#    response = response.replace("\n","<br>")
    print("------------------------")
    print(response)
    namefile = address
    
    #return render_template('index.html', response=response)

    #request the program for doing the request
    return render_template('index.html',response=response,namefile=namefile)


@app.route("/response/", methods = ['GET','POST'])
def response():
    data = request.form
    #extracting the parameters
    namefile = data["namefile"]
    response = open(namefile+".temp", "r+") 
    targetip, ttlip, route = get_parameters(response)
    print(targetip, ttlip, route )
    num_links = len(route)
    print(data)

    #request the program for doing the request
    return render_template('graph2.html',  targetip=targetip, ttlip= ttlip, route=route, num_links = num_links )

#Start the app
if __name__=="__main__":
    app.secret_key = '879sd3$55cDS'
    app.run(debug=True)

