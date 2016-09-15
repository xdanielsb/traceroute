from __future__ import print_function
import re

url_file = "./200.69.103.254.temp"
file_data = open(url_file, "r+")

#regular expressions
reTargetAddress = r'^Target IP address:(.+)'
reTtl = r'Maximum Time to Live .+:(.+)'
retrace = r'^\d+\s+(.+)'

#Variables
targetip = None
ttlip = None
route = []

#Apply the regular expresions over the result
for line in file_data:
    #line without spaces 
    l= line.rstrip().lstrip()
    targeta = re.search(reTargetAddress, l)
    ttl = re.search(reTtl, l)
    trace = re.search(retrace, l)

    if targeta is not None:        
        for pattern in targeta.groups():
            targetip= pattern
            #print ("target address: ", end =" ")
            #print (pattern);
    if ttl is not None:        
        for pattern in ttl.groups():
            ttlip = pattern
            #print ("ttl", end =" ")
            #print (pattern);
    if trace is not None:        
        for pattern in trace.groups():
            route.append(l)
            #print ("trace", end =" ")
            #print (str(pattern));

print ()
print("target ip: "+targetip)
print("ttl: "+ ttlip)
print("route: ")
for r in route:
    print (r)




