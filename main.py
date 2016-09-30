"""
" This script helps to manage all the pages
"""

#Import the framework
from __future__ import print_function
from flask import Flask, render_template, request, send_from_directory
import os
import os.path
from process_file import get_parameters 

#Create the app
app = Flask(__name__, static_folder='static')

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
    source2 = data["source2"]
    
    print(data)
    phantom = "export PATH=$PATH:/opt/phantom/bin/ &&  "
    casper = "/opt/casperjs/bin/casperjs "
    
    if source=="" and source2 =="":
        print("1-----------")
        return render_template('index.html',response="It is necesary choose a destiny",namefile="")
    elif source2 != "":
        print("2-----------")
        script = "~/Documents/myProjects/scripting/logic/casper/global-crossing.js "
        argumentsource = " --source="+source2
    else:
        print("3-----------")
        script = "~/Documents/myProjects/scripting/logic/casper/eastlink.js "
        argumentsource = " --source='"+source+"'"
    
    argumentip = "--addr="+address
    
    pipe = " | tee "+address+"-"+argumentsource[10:]+".temp"
    command = phantom + casper + script + argumentip + argumentsource + pipe 
    

    #print (command)
    #execute the command
    

    if (os.path.isfile("./"+address+"-"+argumentsource[10:]+".temp")):
        pass
    else:
        os.system(command)
    #reading the answer
    n = "./"+address+"-"+argumentsource[10:]+".temp"
    response = open(n, "r+").read() 
    print(n)
    print(response)
    namefile = address+"-"+argumentsource[10:]
    namefile = namefile.replace("'","")
    
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


@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory("/home/daniel/Documents/myProjects/scripting/", filename+".temp")


#Start the app
if __name__=="__main__":
    app.secret_key = '879sd3$55cDS'
    app.run(debug=True)

