from coursebase.extractors.data import get_soup_post, read_config, read_cache


def ext_tags(cell):
    return [
        tag
        for tag in cell.find_all("span")
        if tag.has_attr("class") and not tag.has_attr("style")
    ]


def process_str(tag):
    tmp = tag.text.replace("\n", " ").replace("ID Bekleniyor.", "")
    return (tmp[:9] + " " + tmp[9:]).strip() + " "


def ext_row_text(cell):
    return "".join([process_str(tag) for tag in ext_tags(cell)]).strip()


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
            courses["Monday"].append(ext_row_text(cells[1]))
            courses["Tuesday"].append(ext_row_text(cells[2]))
            courses["Wednesday"].append(ext_row_text(cells[3]))
            courses["Thursday"].append(ext_row_text(cells[4]))
            courses["Friday"].append(ext_row_text(cells[5]))
            courses["Saturday"].append(ext_row_text(cells[6]))
            courses["Sunday"].append(ext_row_text(cells[7]))
    return courses


def gen_post_data() -> dict:
    return {"courses[]": [read_cache()[look] for look in read_config()]}
