import re
import pandas as pd
from coursebase.extractors.data import get_soup_post, read_config, read_cache

def ext_tags(cell):
    return [
        tag for tag in cell.find_all("span")
        if tag.has_attr("class") and not tag.has_attr("style")
    ]


def process_str(tag):
    p = re.match(r'(?P<name>\b[\w\s]+\.\d)(?P<id>[\w\d\s]+)\b\s*', tag.text)
    return p.groupdict()['name'] + " " + p.groupdict()['id'] + " "


def ext_row_text(cell):
    return "".join([process_str(tag) for tag in ext_tags(cell)]).strip()


def ext_cells(cells):
    return [cells[0].find(text=True)
            ] + [ext_row_text(cells[i]) for i in range(1, 8)]


def get_schedule():
    from coursebase import URL_COURSEBASE

    head = [
        "Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"
    ]

    soup = get_soup_post(URL_COURSEBASE, gen_post_data())
    html_tbl = soup.find("table", class_="table table-bordered text-center")

    return pd.DataFrame([
        ext_cells(cell) for cell in [
            cells for cells in
            [row.find_all("td")
             for row in html_tbl.find_all("tr")] if len(cells) == 8
        ]
    ],
                        columns=head)


def gen_post_data() -> dict:
    return {"courses[]": [read_cache()[look] for look in read_config()]}
