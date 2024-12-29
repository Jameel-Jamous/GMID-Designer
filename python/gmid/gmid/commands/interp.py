import click
from gmid.DFManager import DFManager
    
def main(*args, **kwargs):
    pass 

@click.command(name='interp')
@click.argument('value', required=False)
@click.option('--p', '--param', multiple=True, required=False)
@click.option('--a', '--annotated', is_flag=True, default=False, required=False)
def main(*args, **kwargs):
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")