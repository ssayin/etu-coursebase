import requests
import json
from bs4 import BeautifulSoup
from coursebase import CONFIG_FILE, CACHE_FILE


def get_soup(url):
    with requests.get(url) as page:
        if page.status_code == 200:
            return BeautifulSoup(page.content, "lxml")


def get_soup_post(url, data):
    with requests.post(url, data) as page:
        return BeautifulSoup(page.content, "lxml")


class CacheData:
    def __init__(self):
        pass

    def write(self) -> None:
        from coursebase import URL_COURSEBASE

        soup = get_soup(URL_COURSEBASE)
        courses: dict = []
        for a in [
            x
            for x in soup.find_all("select")
            if x.has_attr("name") and x["name"] == "courses[]"
        ]:
            for b in a.find_all("option"):
                courses.append({"i": b["value"], "n": b.text})

        with open(CACHE_FILE, "w") as out:
            json.dump({"c": courses}, out, ensure_ascii=False)

    def read(self) -> dict:
        with open(CACHE_FILE, "r") as f:
            return dict((key["n"], key["i"]) for key in json.loads(f.read())["c"])


class ConfigData:
    def __init__(self):
        pass

    def write(self, courses: list):
        with open(CONFIG_FILE, "w") as f:
            json.dump({"lookFor": courses}, f, ensure_ascii=False)

    def read(self):
        with open(CONFIG_FILE, "r") as f:
            return json.loads(f.read())["lookFor"]
