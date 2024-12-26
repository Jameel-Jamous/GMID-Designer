import click

@click.command(name="hello")
def main(name):
    """Hello: Says Hello"""
    click.echo(f"Hello World")