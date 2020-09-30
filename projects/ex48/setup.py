try:
    form setuptools import setup
except ImportError:
    from distuntils.core import setup

config = {
    'description': 'My Project',
    'author': 'Kevin Bai',
    'url': 'URL to get at it.'
    'download_url': 'Where to download it.',
    'author_email': 'kevinbai@berkeley.edu,',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48',
}
setup(**config)
