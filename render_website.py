from livereload import Server

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from os import sep
from more_itertools import chunked
from pathlib import Path
from math import ceil


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

media_path = Path('media')
with open(media_path / 'books.json', encoding='utf8') as file:
    books = json.load(file)

pages_path = Path('pages')
pages_path.mkdir(parents=True, exist_ok=True)
books_per_page = 20
columns_per_page = 2
max_page_num=ceil(len(books) / books_per_page)
for page_num, books in enumerate(chunked(books, books_per_page), 1):
    rendered_page = template.render(
        chunked_books=chunked(books, columns_per_page),
        sep=sep,
        current_page_num=page_num,
        max_page_num=max_page_num,
    )

    with open(pages_path / f'index{page_num}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
 
def on_reload():
    print('Site rebuilt')

on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
