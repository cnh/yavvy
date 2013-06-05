#AUTHTOKEN=6d8c8ddfbf9c6ed53c0cc4de81a5e6f7
#adapted from
#http://www.zoho.com/crm/help/api/examples.html#3._Fetch_Records_from_the

import urllib
import urllib2
import os
import xml.dom.minidom

print os.getcwd()
module_name = 'Leads'
authtoken = '6d8c8ddfbf9c6ed53c0cc4de81a5e6f7'
params = {'authtoken':authtoken,'scope':'crmapi'}
final_URL = "https://crm.zoho.com/crm/private/xml/"+module_name+"/getRecords"
data = urllib.urlencode(params)
request = urllib2.Request(final_URL,data)
response = urllib2.urlopen(request)
xml_response = response.read()
print xml_response

xml = xml.dom.minidom.parseString(xml_response)
print xml.toprettyxml()



import io
import xml.etree.ElementTree as etree

#a_file = io.StringIO(response)
a_file = open('test.xml', mode='w') 
a_file.write(xml_response)
a_file.close()

#b_file = open('test.xml', mode='r') 
#tree = etree.parse(b_file)
tree = etree.ElementTree(file='test.xml')
root = tree.getroot()
print root
#b_file.close()
for elem in tree.iter():
    	print elem.tag, elem.text, elem.attrib

# fast element searching using iterparse

'''
http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
http://effbot.org/zone/element-iterparse.htm

count = 0
for event, elem in ET.iterparse(sys.argv[2]):
    if event == 'end':
        if elem.tag == 'location' and elem.text == 'Zimbabwe':
            count += 1
    elem.clear() # discard the element

print count
'''
