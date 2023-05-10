from livereload import Server

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from os import sep
from more_itertools import chunked


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

with open('books.json', encoding='utf8') as file:
    books = json.load(file)

rendered_page = template.render(
    chunked_books=chunked(books, 2),
    sep=sep
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

def on_reload():
    print('Site rebuilt')

on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
