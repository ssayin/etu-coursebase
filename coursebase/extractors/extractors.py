from bs4 import BeautifulSoup
from coursebase.extractors.data import get_soup_post, ConfigData, CacheData


class CourseTblExtractor:
    def __init__(self):
        pass


def ext1(cell):
    return [
        tag
        for tag in cell.find_all("span")
        if tag.has_attr("class") and not tag.has_attr("style")
    ]


def ext_sub_tbl(cell):
    ret = ""
    for tag in ext1(cell):
        tmp = tag.text.replace("\n", " ").replace("ID Bekleniyor.", "")
        ret += (tmp[:9] + " " + tmp[9:]).strip()
    return ret


def get_schedule():
    from coursebase import URL_COURSEBASE

    courses = {
        "Time": [],
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    soup = get_soup_post(URL_COURSEBASE, gen_post_data())
    html_tbl = soup.find("table", class_="table table-bordered text-center")
    for row in html_tbl.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) == 8:
            courses["Time"].append(cells[0].find(text=True))
            courses["Monday"].append(ext_sub_tbl(cells[1]))
            courses["Tuesday"].append(ext_sub_tbl(cells[2]))
            courses["Wednesday"].append(ext_sub_tbl(cells[3]))
            courses["Thursday"].append(ext_sub_tbl(cells[4]))
            courses["Friday"].append(ext_sub_tbl(cells[5]))
            courses["Saturday"].append(ext_sub_tbl(cells[6]))
            courses["Sunday"].append(ext_sub_tbl(cells[7]))
    return courses


def gen_post_data() -> dict:
    cache = CacheData()
    config = ConfigData()
    return {"courses[]": [cache.read()[look] for look in config.read()]}
