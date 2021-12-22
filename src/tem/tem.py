from tem.tmpl import TEM_CONFIG_DIR
import argparse
import wora.dynmod
import wora.file
import json
import pathlib

def main():
    parser = argparse.ArgumentParser(description='An all purpose templating program to quickly start projects off with a bang')
    parser.add_argument('fp', type=str, help='Filepath to template directory')
    args = parser.parse_args()
    fp = args.fp

    cfg = wora.file.read_file(pathlib.Path(f'{TEM_CONFIG_DIR}/templates.json'))
    if (cfg is not None):
        o = json.loads(cfg)
        for name, tmplfp in o['templates'].items():
            if fp == name:
                fp = pathlib.Path(tmplfp).expanduser()
                break

    template = wora.dynmod.module_from_file("template", f'{fp}/template.py')
    template.bang(fp)
