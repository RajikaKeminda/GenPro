import os
import click
import subprocess
from ..model.prompt import prompt, change_prompt


@click.group()
def cli():
    pass


@click.command()
def start():
    cmd_path = os.path.dirname(os.path.abspath(__file__))
    www_path = os.path.join(os.path.dirname(cmd_path), 'www')
    os.chdir(www_path)

    subprocess.run(['yarn', 'start'], check=True)


@click.command()
@click.argument('msg')
def ask(msg):
    prompt(msg)


@click.command()
@click.argument('msg')
def change(msg):
    change_prompt(msg)


cli.add_command(start)
cli.add_command(ask)
cli.add_command(change)