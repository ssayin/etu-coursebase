import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import click

url = 'http://kayit.etu.edu.tr/rapor/web/index.php/Program2020guz/coursebase'

def ext1(cell):
    return [ tag for tag in cell.find_all('span') 
            if tag.has_attr('class') and not tag.has_attr('style') ]

def e1(cell):
    ret = ''
    for tag in ext1(cell):
        tmp = tag.text.replace('\n', ' ').replace('ID Bekleniyor.', '')
        ret += (tmp[:9] + " " + tmp[9:]).strip()
    return ret

def ext_sub_tbl(cell, extractor = e1):
    return extractor(cell)

def get_course_dataframe_h(html_tbl):
    courses = {'Time': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [], 
                'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    for row in html_tbl.find_all('tr'):
        cells=row.find_all('td')
        if len(cells)==8:    
            courses['Time'].append(cells[0].find(text=True))
            courses['Monday'].append(ext_sub_tbl(cells[1]))
            courses['Tuesday'].append(ext_sub_tbl(cells[2]))
            courses['Wednesday'].append(ext_sub_tbl(cells[3]))
            courses['Thursday'].append(ext_sub_tbl(cells[4]))
            courses['Friday'].append(ext_sub_tbl(cells[5]))
            courses['Saturday'].append(ext_sub_tbl(cells[6]))
            courses['Sunday'].append(ext_sub_tbl(cells[7]))
    return pd.DataFrame (data = courses)

def get_html_tbl(): 
    with requests.post(url, data = gen_post_data()) as page:
        soup = BeautifulSoup(page.content, 'lxml')
        return soup.find('table', class_='table table-bordered text-center')

def get_course_dataframe():
    return get_course_dataframe_h(get_html_tbl())

def gen_course_lookup() -> dict:
    with click.open_file("data.json", "r") as f:
        return dict ((key['n'], key['i']) for key in json.loads(f.read())['c'])

def gen_post_data() -> dict:
    return ( {'courses[]': [gen_course_lookup()[look] for look in read_courses_from_json()]} )

def read_courses_from_json():
    with click.open_file("courses.json") as f:
        return json.loads(f.read())['lookFor']
