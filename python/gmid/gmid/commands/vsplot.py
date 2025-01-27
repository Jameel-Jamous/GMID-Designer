import click

from gmid.contexts.VSPlotOptionContext import VSPlotOptionContext


@click.command(name="vsplot")
@click.argument("yx_header", nargs=2, required=True)
@click.option("-o", "--output-as", required=False, type=str, help="Outputs as a pdf.")
def main(*args, **kwargs):
    """Plot a header against another header.\n
    Run \'view -h\' to view all possible headers to use."""
    #    click.echo("It Worked")
    #    for item in args:
    #        click.echo(f"{item}")

    #    for key, value in kwargs.items():
    #        click.echo(f"{key}: {value}")

    VSPlotOptionContext(args, kwargs).execute().print()
