import click

@click.command(name='plot')
@click.argument('header', required=True)
@click.option('-p', '--pdf', is_flag=True, required=False, help="Outputs as a pdf." )
@click.option('-j', '--jpeg', is_flag=True, required=False, help="Outputs as a jpeg.")
@click.option('-h', '--head', multiple=True, required=False, help="Header to plot." )
def main(*args, **kwargs):
    """Plot a header against 'gmid'.\n
    Run \'view -h\' to view all possible header to use. """
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")