import os
from rich.syntax import Syntax
from rich.console import Console

from . import get_file_structure

def prompt(message):
    console = Console()

    struct_str = get_file_structure(os.getcwd())
    console.print(struct_str)