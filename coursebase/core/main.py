from coursebase.extractors.extractors import get_schedule
from coursebase.filter.util import get_day_index, get_time_index
from coursebase.extractors.data import CacheData
from coursebase import CACHE_DIR, CONFIG_DIR   
import os
import os.path
import pandas as pd
import sys

def try_to_access(path):
    try:
        absp = os.path.abspath(path)
    except OSError as err:
        sys.stderr.write('Cannot access {0}\n{1}\n'.format(absp, str(err)))
        sys.exit(1)
    if os.path.exists(absp) and not os.access(absp, os.W_OK):
        #sys.stderr.write('No write access in {0}\n'.format(absp))
        sys.exit(1)
    return absp

def main():
    cache = try_to_access(CACHE_DIR)
    config = try_to_access(CONFIG_DIR)

    if not os.path.isfile('{0}/config.json'.format(config)):
        sys.stderr.write('Please create config.json in {0}\n'.format(str(config)))
        sys.exit(1)

    if not os.path.isfile('data.json'):
        dt = CacheData()
        dt.write()

    args, options = parse()
    df = pd.DataFrame(get_schedule())
    if args.today and args.now:
        print ("--today and --now are mutually exclusive")
        sys.exit(0)
    if args.today:
        df = df.iloc[:,[0, get_day_index()]]
        print(df.to_string(index=False))
    elif args.now:
        df = df.iloc[get_time_index(), get_day_index()]
        if df == "":
            print ("Great news, no class at the moment.\n")
        else:
            print (df)
    else:
        print(df.to_string(index=False))

def parse():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False)
    parser.add_option("-t", "--today", action="store_true", dest="today", default=False)
    parser.add_option("-n", "--now", action="store_true", dest="now", default=False)
    options, args = parser.parse_args()
    return options, args
