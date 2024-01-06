import os
import re

def get_file_structure(path):
        
        tree_str = """"""

        for root, dirs, files in os.walk(path):
            if re.search("node_modules", root): continue
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            # print('{}{}/'.format(indent, os.path.basename(root)))
            tree_str = tree_str + '{}{}/\n'.format(indent, os.path.basename(root))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                # print('{}{}'.format(subindent, f))
                tree_str = tree_str + '{}{}\n'.format(subindent, f)

        return tree_str


def get_file_contents(path):
        model = []

        for root, dirs, files in os.walk(path):
            if re.search("node_modules", root): continue
            if re.search("src", root): 
                print(root, os.path.basename(root), os.path.dirname(root))
                for f in files:
                    code = ""
                    with open(f"{root}/{f}", "r") as file:
                        code = file.read()

                    model.append({                    
                        "dir": os.path.basename(os.path.dirname(root)),
                        "path": f"{os.path.basename(os.path.dirname(root))}/{os.path.basename(root)}",
                        "file": f,
                        "content" : code
                    })

        return model      