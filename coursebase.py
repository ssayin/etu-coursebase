import click
import pandas as pd
from extractors import get_course_dataframe
from fetcher import create_course_json 
from util import get_time_index
from util import get_day_index

@click.group()
def cli():
    """ A command line interface for ETu's coursebase.
        
        Please run coursebase generate if running for the first time.
    """
    pass

@cli.command()
@click.option('--today', '-t', default=False, is_flag=True, help='Filter the courses by current day')
@click.option('--now', '-n', default=False, is_flag=True, help='Filter the courses by current time')
def schedule(today, now):
    """ Print course schedule and exit.

    Requires data.json table to exist in current directory.
    """
    if today and now:
        return
    
    df = get_course_dataframe()    
    
    if today:
        df = df.iloc[:,[0,get_day_index()]]
    if now:
        df = df.iloc[get_time_index(),get_day_index()]
        return
    
    click.echo(df.to_string(index=False))

@cli.command()
def generate():
    """ Generate data.json. 
    
    Fetches and dumps course ids required for POST requests.
    """
    create_course_json()

if __name__ == '__main__':
    cli()
