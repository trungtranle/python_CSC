import xml.dom.minidom as minidom
import os.path

class CD(object):
    def __init__(self, ten, ca_sy, so_bai_hat, gia_thanh):
        self.ten = ten
        self.ca_sy = ca_sy
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh

def ThemCD(filename ,cd):
    if os.path.isfile(filename):
        f = minidom.parse(filename)
        root = f.documentElement
    else:
        f = minidom.Document()
        root = f.createElement('cds')
        f.appendChild(root)
    child_node = f.createElement('cd')
    child_node.setAttribute('ten', cd.ten)
    root.appendChild(child_node)
    
    ca_sy = f.createElement('ca_sy')
    ca_sy.appendChild(f.createTextNode(cd.ca_sy))
    child_node.appendChild(ca_sy)
    
    so_bai_hat = f.createElement('so_bai_hat')
    so_bai_hat.appendChild(f.createTextNode(cd.so_bai_hat))
    child_node.appendChild(so_bai_hat)

    gia_thanh = f.createElement('gia_thanh')
    gia_thanh.appendChild(f.createTextNode(cd.gia_thanh))
    child_node.appendChild(gia_thanh)
    
    f.writexml(open(filename, 'w'), indent = '', addindent = '', newl = '')

cd = CD('3', '3', '3', '3')

ThemCD('python_nangcao/cd.xml', cd)

