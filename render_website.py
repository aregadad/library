from livereload import Server

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from os import sep
from more_itertools import chunked
from pathlib import Path


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

with open('books.json', encoding='utf8') as file:
    books = json.load(file)

pages_path = Path('pages')
pages_path.mkdir(parents=True, exist_ok=True)
for index, books in enumerate(chunked(books, 20), 1):
    rendered_page = template.render(
        chunked_books=chunked(books, 2),
        sep=sep
    )

    with open(pages_path / f'index{index}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

def on_reload():
    print('Site rebuilt')

on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
