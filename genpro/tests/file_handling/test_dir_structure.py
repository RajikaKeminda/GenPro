import unittest
import os
import re


class TestStructure(unittest.TestCase):
    def test_structure(self):
        startpath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'www')
        
        tree_str = """"""

        for root, dirs, files in os.walk(startpath):
            if re.search("node_modules", root): continue
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            # print('{}{}/'.format(indent, os.path.basename(root)))
            tree_str = tree_str + '{}{}/\n'.format(indent, os.path.basename(root))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                # print('{}{}'.format(subindent, f))
                tree_str = tree_str + '{}{}\n'.format(subindent, f)

        return tree_str
    