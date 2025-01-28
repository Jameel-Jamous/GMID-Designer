import click

from gmid.commands import interp, plot, setter, view, vsplot


@click.group()
def cli():
    """A CLI tool for performing SSI/MSI current efficiency (GMID) calculations and visualizations"""
    pass


cli.add_command(view.main)
cli.add_command(setter.main)
cli.add_command(interp.main)
cli.add_command(plot.main)
cli.add_command(vsplot.main)

if __name__ == "__main__":
    cli()
