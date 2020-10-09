from coursebase.extractors.extractors import get_schedule
from coursebase.filter.util import get_day_index, get_time_index
import pandas as pd
import sys
from pathlib import Path
from coursebase import CONFIG_FILE, CACHE_FILE, CONFIG_DIR, CACHE_DIR
from typing import Iterator
from coursebase.extractors.data import CacheData
import logging

log = logging.getLogger()
console = logging.StreamHandler()
log.addHandler(console)


def ensure_paths_exist(paths: Iterator[Path]) -> None:
    for path in paths:
        if not path.exists() or not path.is_dir():
            log.info("Creating directory {0}".format(path))
            path.mkdir()


def main():
    options, args = parse()
    ensure_paths_exist([CONFIG_DIR, CACHE_DIR])

    if not CACHE_FILE.is_file():
        log.info("Downloading course cache.")
        CacheData().write()
        log.info("Downloaded course cache.")

    if not CONFIG_FILE.is_file():
        log.error("Please create {0}".format(CONFIG_FILE))
        sys.exit(1)

    df = pd.DataFrame(get_schedule())
    if options.today:
        df = df.iloc[:, [0, get_day_index()]]
    elif options.now:
        df = df.iloc[get_time_index(), get_day_index()]
        if df == "":
            print("Great news, no class at the moment.")
            sys.exit(0)
        else:
            print(df)
            sys.exit(0)

    print(df.to_string(index=False))


def parse():
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option(
        "-v", "--verbose", action="store_true", dest="verbose", default=False
    )
    parser.add_option("-t", "--today", action="store_true", dest="today", default=False)
    parser.add_option("-n", "--now", action="store_true", dest="now", default=False)

    options, args = parser.parse_args()

    if options.verbose:
        console.setLevel(logging.INFO)
        log.setLevel(logging.INFO)
    if options.today and options.now:
        print("--today and --now are mutually exclusive")
        sys.exit(0)

    return options, args
