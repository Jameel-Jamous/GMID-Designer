import click

from gmid.commands import hello
from gmid.commands import link
from gmid.commands import setter
from gmid.commands import interp
from gmid.commands import plot
from gmid.commands import vsplot

@click.group()
def cli():
    """My CLI Tool"""
    pass

cli.add_command(hello.main)
cli.add_command(link.main)
cli.add_command(setter.main)
cli.add_command(interp.main)
cli.add_command(plot.main)
cli.add_command(vsplot.main)

if __name__ == "__main__":
    cli()