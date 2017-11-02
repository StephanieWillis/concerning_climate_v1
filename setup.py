try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author' : 'Stephanie Willis',
    'url': 'URL to get it at.,'
    'download_url' : 'Where to download it.',
    'author_email' : 'stephaniewillis808@gmail.com'
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['concerning_climate],
    'scripts': [],
    'name': 'concerning_climate'
}

setup(**config)
