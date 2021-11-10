import os
import argparse
import importlib.util
from jinja2 import Template

def main():
    parser = argparse.ArgumentParser(description='An all purpose general templating program, and project starter program')
    parser.add_argument('fp', type=str, help='Filepath to template file')
    args = parser.parse_args()

    fp = args.fp

    def read_file(fname: str) -> str:
        file = open(fname, 'r')
        res = file.read()
        file.close()
        return res


    t = Template(read_file(fp))
    dirname = os.path.dirname(fp)

    def module_from_file(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    template = module_from_file("template", f'{dirname}/template.py')
    template.bang(t, fp)
