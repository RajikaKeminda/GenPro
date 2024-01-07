import unittest
from openai import OpenAI

client = OpenAI(api_key="")

class TestPrompt(unittest.TestCase):
    def test_prompt(self):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I want you to act as a code reviewer. Analyze the following code snippet and identify any mistakes or issues. Please regenerate the corrected code snippet without providing personal opinions. If you cannot analyze the code, please return the given code as the response. dont return any additional text give only code. its very important because i directly use your response to replace a script file"},
            {"role": "user", "content": """def print_hello():
    name
    print("Hello world")"""},
    {"role": "system", "content": """
        def print_hello():
            name = None
            print("Hello world")
    """},
    {"role": "user", "content": """
    import os
    import unitte

    class TestReadFile(unittest.TestCase):
        def test_read(self):
            with open(os.path.join(os.path.dirname(__file__), "sample.py"), "r") as file:
                code = file.read()
                code = code.replace("Hello !", "Hello world")
                print(code)

            with open(os.path.join(os.path.dirname(__file__), "sample.py"), "w") as file:
                file.write(code)
    """}
        ]
        )

        print(completion.choices[0].message.content)