import click 

@click.group()
@click.option('--debug/--no-debug' , default=False)
@click.pass_context
def cli(ctx,debug):
    #ensure that ctx.obj exist and is a dict ()
    ctx.ensure_object(dict)
    click.echo(debug)
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context
def sync(ctx):
    click.echo("Debug is %s" % (ctx.obj['DEBUG'] and 'on' or 'off'))

if __name__ == "__main__":
    cli(obj={})