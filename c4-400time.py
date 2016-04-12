import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
pattern_str = re.compile(r'and the next nothing is (\d+)$')
num = "12345"

for i in range(0,400+1):  
    rurl = (url+"?nothing=%s")%(num)  
    str = urllib2.urlopen(rurl).read()
    print str
    match = re.findall(pattern_str,str)
    if match:
        num = match[0]
    else:
        print "not found"
        break
    
    