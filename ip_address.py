import os

def get_ip_address(url):
    command = "nslookup " + url
    process = os.popen(command)
    results = str(process.read())
    #marker = results.find(' Address: ') + 12
    #return results[marker:].splitlines()[0]
    return results

#print(get_ip_address('itviec.com'))