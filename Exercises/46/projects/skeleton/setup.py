try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Adam',
    'url': 'URL',
    'download_url': 'URL',
    'author_email': 'amiritis@wolfmail.co',
    'version': 0.1,
    'install_requires': ['nose'],
    'packages':['NAME'],
    'scripts':, [],
    'name': "LPTHW Skeleton"
    }

setup (**config)
