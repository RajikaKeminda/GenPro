import click

@click.group()
def cli():
    pass


@click.command()
def start():
    print("pbot starting...")


cli.add_command(start)