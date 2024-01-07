from rich.console import Console
from rich.syntax import Syntax

console = Console()

txt = """
class TestStructure(unittest.TestCase):
    def test_structure(self):
        startpath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'www')
        print(startpath)
        for root, dirs, files in os.walk(startpath):
            if re.search("node_modules", root): continue
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level) # this should be remove
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
"""
syntax = Syntax(txt, "python", theme="monokai", line_numbers=True)
console.print(syntax)