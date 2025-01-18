import click

from gmid.contexts.InterpOptionContext import InterpOptionContext


@click.command(name="interp")
@click.argument("header", required=True)
@click.option(
    "-h", "--head", multiple=True, required=False, help="Header to interpolate."
)
@click.option(
    "-a",
    "--annotated",
    is_flag=True,
    default=False,
    required=False,
    help="Displays an Annotated Plot",
)
def main(*args, **kwargs):
    """Interpolate a header at a value established in \'set\'.\n
    Run \'view -h\' to view all possible header to use."""
    # For Debugging
    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")

    context = InterpOptionContext(args, kwargs)
    click.echo(context.execute().print())
