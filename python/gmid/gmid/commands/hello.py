import click

@click.command(name="hello")
def main():
    """Hello: Says Hello"""
    click.echo(f"Hello World")