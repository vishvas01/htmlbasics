import lxml.etree as ET

xml = ET.parse('student_details.xml')
schema = ET.XMLSchema(file='student_details.xsd')

if schema.validate(xml):
    print('The provided XML is valid')
else:
    print('The provided XML is invalid')
    print(schema.error_log)
