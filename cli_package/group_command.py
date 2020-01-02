#nesting command with click 
# group_command  COMMAND
#multiple subcommands can be attached
import click 

@click.group()
def cli():
    pass 

@click.command()
def initdb():
    click.echo("Initialized database")

@click.command()
def dropdb():
    click.echo("Dropped the database")

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == "__main__":
    cli()