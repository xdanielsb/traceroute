"""
" Daniel Santos 
" September, 2016
" This script helps to manage all the pages
"""

#Import the framework
from __future__ import print_function
from flask import Flask, render_template, \
        request, send_from_directory, flash
import os
import os.path
from process_file import get_parameters  # file for proccess the response
from servers import get_servers


#Create the app
app = Flask(__name__, static_folder='static')
servers = get_servers()

#Add a wrapper for the home page
@app.route('/')
def homepage():
    #request the program for doing the request
    return render_template('index.html', servers = servers)


@app.route('/traceroute/', methods = ['GET','POST'])
def traceroute():
    data = request.form
    #extracting the parameters of the form
    address= data["ip"]
    source = data["source"]
    source2 = data["source2"]
    is_university = False
    
    #Help me to run the code in the university
    if is_university:
        path = "/home/laboratorio/Documentos/traceroute/"
    else:
        path = "~/Documents/myProjects/scripting/"
    
    #this is the variable for phantom 
    phantom = "export PATH=$PATH:"+path+"engines/phantom/bin/"
    os.system(phantom)
    
    #this is the location of phantom js
    casper = path+"engines/casperjs/bin/casperjs "
    
    #identifies the source
    if source=="" and source2 =="":
        print("1-----------")
        return render_template('index.html',response="It is necesary choose a destiny",namefile="")
    elif source2 != "":
        print("2-----------")
        script = path+"logic/casper/global-crossing.js "
        argumentsource = " --source="+source2
    else:
        print("3-----------")
        script = path+"logic/casper/eastlink.js "
        argumentsource = " --source='"+source+"'"
    
    #Process the filename
    namefile = address+"-"+argumentsource[10:]
    namefile = namefile.replace("'","")
    namefile = namefile.replace(" ","")
    namefile = namefile.replace("(","")
    namefile = namefile.replace(")","")
    
    #ip address 
    argumentip = "--addr="+address
    
    #help me to save  the file for later process 
    pipe = " | tee "+namefile+".temp"
    command =  casper + script + argumentip + argumentsource + pipe 
    
    #Check if the file exist
    if (os.path.isfile("./"+namefile+".temp")):
        pass
    else:
        os.system(command)

    #reading the answer
    response = open(namefile+".temp", "r+").read() 
    flash("The answeralready be prepared")
    return render_template('index.html',response=response,namefile=namefile)


@app.route("/response/", methods = ['GET','POST'])
def response():
    data = request.form
    print(data)
    if len(data)>0:
        #extracting the parameters
        namefile = data["namefile"]
        response = open(namefile+".temp", "r+") 
        targetip, ttlip, route = get_parameters(response)
        num_links = len(route)
        #request the program for doing the request
        return render_template('graph2.html',  targetip=targetip, ttlip= ttlip, route=route, num_links = num_links )
    return render_template('graph2.html')


#helps to download the file
@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory("~/Documents/myProjects/scripting/", filename+".temp")


#Start the app
if __name__=="__main__":
    app.secret_key = '879sd3$55cDS'
    app.run(debug=True)

