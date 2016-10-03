"""
" Daniel Santos 
" September, 2016
" This script helps to manage all the pages
"""

#Import the framework
from __future__ import print_function
from flask import Flask, render_template, \
        request, send_from_directory, flash, session
import os
import os.path
from process_file import get_parameters  # file for proccess the response
from servers import get_servers
from request_post import send_post


#Create the app
app = Flask(__name__, static_folder='static')

app.secret_key = '879sd3$55cDSeouae345euk5634$#%HDIDIHT($#'
app.config['SESSION_TYPE'] = 'filesystem'

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
    
    #capture the data
    source = data["source"]
    source2 = data["source2"]
    source3 = data["source3"]

    #just for put the project in production 
    is_university = False
    
    #Help me to run the code in the university
    if is_university:
        path = "/home/laboratorio/Documentos/traceroute/"
    else:
        path = "~/Documents/myProjects/scripting/"
    
    #this is the variable for phantom 
    phantom = "export PATH=$PATH:"+path+"engines/phantom/bin/"
    a = "export PATH=$PATH:~/Documents/myProjects/scripting/engines/phantom/bin/"
    os.system(phantom)
    
    #this is the location of phantom js
    casper = path+"engines/casperjs/bin/casperjs "
    
    #identifies the source
    if source=="" and source2 =="" and source3 =="":
        return render_template('index.html',response="It is necesary choose a destiny",namefile="")
    elif source2 != "":
        script = path+"logic/casper/global-crossing.js "
        argumentsource = " --source="+source2
    elif source != "":
        script = path+"logic/casper/eastlink.js "
        argumentsource = " --source='"+source+"'"
    else: 
        script = ""
        argumentsource = " --source="+source3
    
    #Process the filename
    namefile = address+"-"+argumentsource[10:]
    namefile = namefile.replace("'","")
    namefile = namefile.replace(" ","")
    namefile = namefile.replace("(","")
    namefile = namefile.replace(")","")
    
    #ip address 
    #help me to save  the file for later process 
    argumentip = "--addr="+address
    pipe = " | tee "+namefile+".temp"

    command =  casper + script + argumentip + argumentsource + pipe 
    print(command)
    
    #Check if the file exist
    if (os.path.isfile("./"+namefile+".temp") or source3 != ""):
        datos = {}
        host = "http://www.cogentco.com/lookingglass.php"
        datos['LOC'] = source3
        datos['DST'] = address
        data = send_post(datos, host)
        data = data[data.find("<pre>")+5:data.find("</pre>")]
        print (data)
        # Open a file
        fo = open(namefile+".temp", "wb")
        fo.write(data);
        # Close opend file
        fo.close()
    else:
        os.system(command)

    #reading the answer
    response = open(namefile+".temp", "r+").read() 
    response2 = response.replace( "\n", "---n")
    flash("The answer already be prepared")
    return render_template('index.html',response=response,namefile=response2, servers = servers)


@app.route("/response/", methods = ['GET','POST'])
def response():
    data = request.form
    #print(data)
    if len(data)>0:
        #extracting the parameters
        response = data["namefile"]
        #print(response.split("    "))
        targetip, ttlip, route = get_parameters(response.split("---n"))
        num_links = len(route)
        #request the program for doing the request
        return render_template('graph2.html',  targetip=targetip, ttlip= ttlip, route=route, num_links = num_links )
    return render_template('graph2.html')


#helps to download the file
@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory("~/Documents/myProjects/scripting/", filename+".temp")


if(__name__=="__main__"):
    app.run(debug=True)


