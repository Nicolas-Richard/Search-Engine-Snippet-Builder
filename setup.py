try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Snippet highlighter - Yelp Coding Challenge',
    'author': 'Nicolas Richard',
    'url': '',
    'download_url': '',
    'author_email': 'NicolasRichard3@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'stemming', 'wsgiref'],
    'packages': ['snippet_highlighter'],
    'scripts': [],
    'name': 'snippet_highlighter'
}

setup(**config)