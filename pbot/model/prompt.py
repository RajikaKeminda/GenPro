import os
from rich.syntax import Syntax
from rich.console import Console

from . import get_file_structure

def prompt(message):
    console = Console()

    console.print(message)