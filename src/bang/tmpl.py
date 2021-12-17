from jinja2 import Template
from wora.file import read_file
from pathlib import Path
import plumbum

def to_path(fp):
    if isinstance(fp, Path):
        return fp
    elif isinstance(fp, str):
        return Path(fp)

def render(src, tmpl_name, vardict):
    tmpl = Template(read_file(str(Path(src) / tmpl_name)))
    res = tmpl.render(vardict)
    return res

def output(dest, tmpl_name, tmpl):
    dest = str(to_path(dest) / tmpl_name)
    (plumbum.cmd.echo[tmpl] > dest)()

def promptf(prompt: str, val=''):
    return input(prompt.format(val)) or val
