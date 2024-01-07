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
                for f in files:
                    if re.search(".svg", f): continue
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


def write_code(path, code):
        
        actual_path = None
        for root, dirs, files in os.walk(os.getcwd()):
            if re.search("node_modules", root): continue
            if re.search("src", root):
                for f in files:
                     abs_path = f"{root}/{f}"
                     if re.search(path, abs_path):
                          actual_path = abs_path
                          break
        
        if actual_path is None:
             raise "Cannot find file path"
        

        with open(actual_path, "w") as file:
            file.write(code)


def create_file(dir, file_name, code):
        
        actual_path = None
        for root, dirs, files in os.walk(os.getcwd()):
            if re.search("node_modules", root): continue
            if re.search("src", root):
                if re.search(dir, root):
                    actual_path = f"{root}/{file_name}"
        
        if actual_path is None:
             raise "Cannot find file path"
      
        with open(actual_path, "w+") as file:
            file.write(code)