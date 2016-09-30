from __future__ import print_function
import re


def get_parameters(file_data):
    
    
    #regular expressions
    reTargetAddress = r'^Target IP address:(.+)'
    reTtl = r'Maximum Time to Live .+:(.+)'
    retrace = r'^\d+\s+(.+)'

    #Variables
    targetip = None
    ttlip = None
    links = []
    route = {}

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
                links.append(l)
                #print ("trace", end =" ")
                #print (str(pattern));
    for i in range(0,len(links)):
        route[i]=links[i]

    """
    print ()
    print("target ip: "+targetip)
    print("ttl: "+ ttlip)
    print("links: ")
    print(links)
    print("route : ")
    print(route)
    """
    return targetip, ttlip, route



