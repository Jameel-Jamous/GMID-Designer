import click
from gmid.commands import hello
from gmid.commands import link

@click.group()
def cli():
    """My CLI Tool"""
    pass

cli.add_command(hello.main)
cli.add_command(link.main)

if __name__ == "__main__":
    cli()