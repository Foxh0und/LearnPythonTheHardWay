try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Building a Lexicon',
    'author': 'Adam',
    'url': 'URL',
    'download_url': 'URL',
    'author_email': 'amiritis@wolfmail.co',
    'version': 1,
    'install_requires': ['nose'],
    'packages':['ex48'],
    'scripts':, [],
    'name': "Advanced User Input"
    }
    
setup (**config)
