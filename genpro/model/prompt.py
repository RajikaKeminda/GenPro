import os
import json
from openai import OpenAI
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.console import Console

from . import get_file_structure, get_file_contents, write_code, create_file

API_KEY=os.environ.get("OPENAI_API_KEY")

def prompt(message):
    client = OpenAI(api_key=API_KEY)
    console = Console()

    with console.status("Analyzing...") as status:
        struct_str = get_file_structure(os.getcwd())
        content = get_file_contents(os.getcwd())

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
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
    

def change_prompt(message):
    client = OpenAI(api_key=API_KEY)
    console = Console()

    with console.status("Working on...") as status:
        struct_str = get_file_structure(os.getcwd())
        content = get_file_contents(os.getcwd())

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                    {"role": "system", "content": "you are a project analyzer, code reviewer, code optimizer and code writer. I give you a full structure of project and file contents. you need to identify the project and modify the codes according to my expressions using given dataset. i directly use your response to change the file content. so you have to give response using specific format that i gives to you. dont use any additional text to the response."},
                    {"role": "system", "content": f"""
                        response_format:
                            {{ "file_path": this should be the path you modified file, "modified_code": modified code should be here }}
                        structure: 
                            {struct_str}

                        file_contents:
                            {content}
                    """},
                    {"role": "user", "content": message}
                ]
            )

        r = completion.choices[0].message.content
        
        try:
            data = json.loads(r)
            file_path = data["file_path"]
            modified_code = data["modified_code"]

            write_code(file_path, modified_code)
        except:
            console.log("Cannot execute")


def create_prompt(message):
    client = OpenAI(api_key=API_KEY)
    console = Console()

    with console.status("Working on...") as status:
        struct_str = get_file_structure(os.getcwd())
        content = get_file_contents(os.getcwd())

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                    {"role": "system", "content": "you are a project analyzer, code reviewer, code optimizer and code writer. I give you a full structure of project and file contents. you need to identify the project and create files and codes according to my expressions using given dataset. i directly use your response to change the file content. so you have to give response using specific format that i gives to you. dont use any additional text to the response."},
                    {"role": "system", "content": f"""
                        response_format:
                            {{ "file_path": this should be the created file path, "dir": this should be the directory path of created file, "file_name": this should be the created file name, "generated_code": generated code should be here }}
                        structure: 
                            {struct_str}

                        file_contents:
                            {content}
                    """},
                    {"role": "user", "content": message}
                ]
            )

        r = completion.choices[0].message.content
        
        try:
            data = json.loads(r)
            dir = data["dir"]
            file_name = data["file_name"]
            generated_code = data["generated_code"]

            create_file(dir, file_name, generated_code)
        except:
            console.log("Cannot execute")