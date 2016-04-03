import urllib2
from xml.dom import minidom
import json

req = urllib2.Request("http://www.example.com")
res = urllib2.urlopen(req)
print res.info()

x = minidom.parseString("""<mytag>contents!<children><item>1</item><item>2</item></children></mytag>""")
print x
print dir(x)
print x.toprettyxml()

j = '{"one":1, "numbers": [1,2,3.5]}'

d = json.loads(j)

print d["numbers"]