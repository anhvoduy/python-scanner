import urllib2
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'            
    res = urllib2.urlopen(path)
    #print(res.info())    
    req = urllib2.Request(path + 'robots.txt', data=None)
    res2 = urllib2.urlopen(req)
    return res2.read()

#print(get_robots_txt('https://www.itviec.com/'))
