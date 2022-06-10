import pathlib
from jinja2 import Environment, FileSystemLoader, select_autoescape

environment = Environment(
    loader=FileSystemLoader(pathlib.Path(__file__).parent / 'templates'),
    autoescape=select_autoescape()
)
