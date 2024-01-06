import os
from openai import OpenAI
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.console import Console

from . import get_file_structure, get_file_contents

client = OpenAI(api_key="")

def prompt(message):
    console = Console()

    struct_str = get_file_structure(os.getcwd())
    content = get_file_contents(os.getcwd())

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "you are a project analyzer and code reviewer. I give you a full structure of project and file contents. you need to identify the project and answer my questions using given dataset."},
                {"role": "system", "content": f"""
                    structure: 
                        {struct_str}

                    file_contents:
                        {content}
                """},
                {"role": "user", "content": message}
            ]
        )

    md = Markdown(completion.choices[0].message.content)
    console.print(md)