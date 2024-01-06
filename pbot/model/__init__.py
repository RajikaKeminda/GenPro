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