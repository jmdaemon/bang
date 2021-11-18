import argparse
import importlib.util

def main():
    parser = argparse.ArgumentParser(description='An all purpose templating program to quickly start projects off with a bang')
    parser.add_argument('fp', type=str, help='Filepath to template directory')
    args = parser.parse_args()
    fp = args.fp

    def read_file(fname: str) -> str:
        file = open(fname, 'r')
        res = file.read()
        file.close()
        return res

    def module_from_file(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    template = module_from_file("template", f'{fp}/template.py')
    template.bang(fp)
