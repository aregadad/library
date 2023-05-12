import json
from math import ceil
from os import sep
from pathlib import Path

import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


parser = argparse.ArgumentParser(
    description='Run personal library server')
parser.add_argument('-j', '--json_dir',
                    help='books.json path (default: media)', default='media')
args = parser.parse_args()                    

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

json_path = Path(args.json_dir)
with open(json_path / 'books.json', encoding='utf8') as file:
    books_descriptions = json.load(file)

pages_path = Path('pages')
pages_path.mkdir(parents=True, exist_ok=True)
books_per_page = 20
columns_per_page = 2
max_page_num = ceil(len(books_descriptions) / books_per_page)
for page_num, books_descriptions in enumerate(chunked(books_descriptions, books_per_page), 1):
    rendered_page = template.render(
        chunked_books_descriptions=chunked(books_descriptions, columns_per_page),
        sep=sep,
        current_page_num=page_num,
        max_page_num=max_page_num,
    )

    with open(pages_path / f'index{page_num}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

server = Server()
server.watch('template.html')
server.serve(root='.')
