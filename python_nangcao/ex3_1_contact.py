import xml.dom.minidom #as minidom

class Contact(object):
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

def read_xml_file(xmlstring):
    f = xml.dom.minidom.parse(xmlstring)
    root = f.documentElement
    if root.hasAttribute('shelf'):
        print(root.getAttribute('shelf'))

    contacts = root.getElementsByTagName('contact')
    i = 1
    list_contact = []
    for contact in contacts:
        if contact.hasAttribute('name') and contact.hasAttribute('phone'):
            contact_i = Contact(contact.getAttribute('phone'), contact.getAttribute('name'))
            list_contact.append(contact_i)
        i += 1
    j = 1
    for item in list_contact:
        print('---Contact %d---' %j)
        print('Name:', item.name)
        print('Phone:', item.phone)
        j += 1

read_xml_file('python_nangcao/contact.xml')
