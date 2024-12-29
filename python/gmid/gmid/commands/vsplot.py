import click
from gmid.DFManager import DFManager


@click.command(name='vsplot')
@click.argument('xdata', required=True)
@click.argument('ydata', required=True)
def main(*args, **kwargs):
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")