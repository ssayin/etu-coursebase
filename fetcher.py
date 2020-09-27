import time
from bs4 import BeautifulSoup
import requests
import json

url = 'http://kayit.etu.edu.tr/rapor/web/index.php/Program2020guz'

def get_soup():
    with requests.get(url) as page:
        if page.status_code == 200:
            return BeautifulSoup(page.content, 'lxml')

def get_select_tags(soup): 
    return [ x for x in soup.find_all('select') if x.has_attr('name') and x['name'] == 'courses[]' ]

def append_courses(c, sel_tags):
    for a in sel_tags:
        for b in a.find_all('option'):
            c.append({'i': b['value'], 'n': b.text})
                            
def dump_course_dict(c):
    with open("data.json", "w") as io:
        json.dump({"c":c}, io, ensure_ascii = False)

def create_course_json():
    c = []
    append_courses(c, get_select_tags(get_soup()))
    dump_course_dict(c)
