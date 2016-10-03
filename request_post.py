import urllib

def send_post(datos, host):
    datos['CMD'] ='T4'
    datos['FKT'] = 'go!'
    response = urllib.urlopen(host,urllib.urlencode(datos)).read()
    return response


if __name__ == "__main__":
    datos = {}
    destiny = 'tyo01'
    source = 'www.facebook.com'
    host = "http://www.cogentco.com/lookingglass.php"
    datos['LOC'] = destiny
    datos['DST'] = source
    
    print( send_post(datos, host))
