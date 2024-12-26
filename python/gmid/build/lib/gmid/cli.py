import click
from gmid.commands import hello

@click.group()
def cli():
    """My CLI Tool"""
    pass

cli.add_command(hello.main)

if __name__ == "__main__":
    cli()