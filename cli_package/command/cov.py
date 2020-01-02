import click 

@click.command()
def cli():
    """
    Run cov  for this coverage test
    """
    click.echo("Coverage command activated")
