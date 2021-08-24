import click


@click.command()
@click.argument("name")
def mycommand(name):
    click.echo("Hi " + name + "!")
