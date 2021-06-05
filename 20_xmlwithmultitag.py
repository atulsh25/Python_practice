import xml.etree.ElementTree as ET
data='''<stuff>
<person_details>
<person>
<name>John</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>
<person>
<name>Meckenzie</name>
<phone type="intl">
+91 223 334 556
</phone>
<email hide="yes"/>
</person>
</person_details></stuff>'''

xml_data=ET.fromstring(data)
lst= xml_data.findall('person_details/person')
for detail in lst:
    print('Name:', detail.find('name').text)
    print('Attr:', detail.find('email').get('hide'))
    print('Phone:', detail.find('phone').text)