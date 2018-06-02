import json
import urllib.request

def read_json_from_url(url_input):
    url = urllib.request.urlopen(url_input)
    DEFAUT_ENCODING = 'utf-8'
    if hasattr(url.headers, 'get_content_charset'):
        encoding = url.headers.get_content_charset(DEFAUT_ENCODING)
    else: 
        encoding = url.headers.getparam('charset') or DEFAUT_ENCODING
    data = json.loads(url.read().decode(encoding))
    return data

def read_json_from_file(dir_input):
    f = open(dir_input, encoding = 'utf-8')
    data = json.load(f)
    f.close()
    return data
    