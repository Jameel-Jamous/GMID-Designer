import click

from gmid.contexts.PlotOptionContext import PlotOptionContext

# TODO: Add an option to plot ranges of the data.
# Example 'gmid plot vov -f min:max will plot
# vov from 'min' to 'max'.


# TODO: Add another option to plot in log scale.
# Example 'gmid plot vov -l' will plot vov in
# log scale


@click.command(name="plot")
@click.argument("header", required=True)
@click.option(
    "-z",
    "--zoom",
    type=str,
    required=False,
    help="Sets the xScale accoriding to a string formatted as 'xmin:xmax'.",
)
@click.option(
    "-o",
    "--output-as",
    type=str,
    required=False,
    help="Outputs plot as format specified by TEXT. See 'matplotlib.pyplot.save_as' to see all supported formats.",
)
@click.option(
    "-h",
    "--head",
    multiple=True,
    required=False,
    help="Adds an additional header to plot.",
)
@click.option(
    "-a", "--annotated", is_flag=True, required=False, help="Adds annotations."
)
def main(*args, **kwargs):
    """Plot a header against 'gmid'.\n
    Run \'view -h\' to view all possible header to use."""
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")

    context = PlotOptionContext(args, kwargs)
    if context.execute().isEmpty():
        click.echo("Strategies were empty")
    else:
        click.echo(f"output: {context.output},\nstratgies: ")
        for item in context.strategies:
            click.echo(f"\t{item.print()}")
        click.echo(f"\noptions: {context.options}")
    click.echo(context.print())
