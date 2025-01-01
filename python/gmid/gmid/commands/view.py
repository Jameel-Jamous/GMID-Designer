import click
import pandas as pd

def displayPaths(paths):
    pathNames = ["Install Path", "Data Path", "Config Path(s)"]
    for path in paths:
        for i, temp in enumerate(path.split(";")):
            click.echo(f"{pathNames[i]}:\n\n\t{temp}\n")

@click.command(name='view')
@click.option('-h', '--head', is_flag=True, required=False, help="Prints a list of available headers.")
@click.option('-p', '--path', is_flag=True, required=False, help="Prints a list of all paths used by the tool.")
@click.option('-v', '--var', type=str, required=False, help="Prints the value of settable variables set for the tool.")
@click.option('-l', '--var-list', is_flag=True, required=False, help="Prints a list of settable variables used by the tool.")
def main(*args, **kwargs):
    """Views headers, variables, and paths used by this tool."""
'''
    context = ViewOptionContext(args, kwargs)
    while(not context.isEmpty()):
        context.execute()
'''
