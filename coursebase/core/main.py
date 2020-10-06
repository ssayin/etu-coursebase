from coursebase.extractors.extractors import get_schedule
from coursebase.filter.util import get_day_index, get_time_index
import pandas as pd
import sys

def main():
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
            print ("Great news, no class at the moment.")
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