import click

from gmid.contexts.ViewOptionContext import ViewOptionContext

# TODO: Refactor this is the 'diffPrint' style for print
# the output string see 'commands/interp.py'


# FIXME: Currently when a path is not available the program crashes!
def displayPaths(paths):
    pathNames = ["Install Path", "Data Path", "Config Path(s)"]
    for path in paths:
        for i, temp in enumerate(path.split(";")):
            click.echo(f"{pathNames[i]}:\n\n\t{temp}\n")


@click.command(name="view")
@click.option(
    "-u",
    "--using-head",
    is_flag=True,
    required=False,
    help="Prints the currently set header.",
)
@click.option(
    "-v",
    "--value",
    is_flag=True,
    required=False,
    help="Prints the currently set value.",
)
@click.option(
    "-p",
    "--path",
    is_flag=True,
    required=False,
    help="Prints a list of all paths currently used by the tool.",
)
@click.option(
    "-a",
    "--all-headers",
    is_flag=True,
    required=False,
    help="Prints a list of all settable headers. This is determined by the data inputted.",
)
def main(*args, **kwargs):
    """Views headers, variables, and paths used by this tool."""
    """
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")
    """
    context = ViewOptionContext(args, kwargs)
    click.echo(context.execute().print())
