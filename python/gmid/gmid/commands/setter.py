import click
from gmid.DFManager import DFManager


@click.command(name='set')
@click.argument('value', required=True)
@click.option('--p', '--param', type=str, required=False)
def main(*args, **kwargs):
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")