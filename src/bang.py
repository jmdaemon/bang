import argparse
import wora.dynmod

def main():
    parser = argparse.ArgumentParser(description='An all purpose templating program to quickly start projects off with a bang')
    parser.add_argument('fp', type=str, help='Filepath to template directory')
    args = parser.parse_args()
    fp = args.fp

    template = wora.dynmod.module_from_file("template", f'{fp}/template.py')
    template.bang(fp)
