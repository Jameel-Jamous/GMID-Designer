import click
import pandas as pd

@click.command()
@click.argument('data_dir')
@click.option('--n', '--nmos', default=True)
@click.option('--p', '--pmos', default=False)
def main(data_dir):
    ret = False
    try:
        ret = False
        #df = pd.read_csv(data_dir)
    except pd.errors.EmptyDataError:
        # Set & Echo Warning
        # Save path
        # Return path has been established 
        ret = True
    except FileNotFoundError:
        # Set & Echo Error
        # Return path has not been established
        ret = False
    
    return ret