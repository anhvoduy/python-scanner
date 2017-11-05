import os
import whois

def get_whois(domain_name):    
    result = whois.whois(domain_name)
    return result

#print(get_whois('itviec.com'))