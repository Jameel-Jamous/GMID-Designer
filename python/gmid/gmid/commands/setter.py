import click

from gmid.contexts.SetOptionContext import SetOptionContext


@click.command(name="set")
@click.argument("value_to_set", required=True)
@click.option("-h", "--head", type=str, required=False, help="Header to set.")
def main(*args, **kwargs):
    """Set a header to be interpolated at a value.\n
    Run \'view -h\' to view all possible header to use."""
    """    
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")
    """
    context = SetOptionContext(args, kwargs)
    click.echo(context.execute().print())
