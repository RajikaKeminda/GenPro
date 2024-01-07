import click
from ..model.prompt import prompt, change_prompt, create_prompt


@click.group()
def cli():
    pass


@click.command()
@click.argument('msg')
def ask(msg):
    prompt(msg)


@click.command()
@click.argument('msg')
def change(msg):
    change_prompt(msg)


@click.command()
@click.argument('msg')
def create(msg):
    create_prompt(msg)


cli.add_command(ask)
cli.add_command(change)
cli.add_command(create)