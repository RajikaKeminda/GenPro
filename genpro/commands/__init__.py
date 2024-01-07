import os
import click
from dotenv import load_dotenv
from ..model.prompt import prompt, change_prompt, create_prompt

load_dotenv()

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


@click.command()
@click.argument('msg')
def set_key(msg):
    env_path = f"{os.path.dirname(os.path.dirname(__file__))}/.env"
    with open(env_path, "w+") as file:
        file.write(f"OPENAI_API_KEY={msg}")


cli.add_command(ask)
cli.add_command(change)
cli.add_command(create)
cli.add_command(set_key)