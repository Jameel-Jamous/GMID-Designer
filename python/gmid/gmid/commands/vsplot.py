import click


@click.command(name='vsplot')
@click.argument('yx_header', required=True)
@click.option('-p', '--pdf', is_flag=True, required=False, help="Outputs as a pdf." )
@click.option('-j', '--jpeg', is_flag=True, required=False, help="Outputs as a jpeg.")
def main(*args, **kwargs):
    """Plot a header against another header.\n
    Run \'view -h\' to view all possible headers to use."""
    click.echo("It Worked")
    for item in args:
        click.echo(f"{item}")

    for key, value in kwargs.items():
        click.echo(f"{key}: {value}")