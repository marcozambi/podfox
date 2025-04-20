from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='podfox',
    version='0.2.0',
    description='Podcatcher for the terminal',
    url='https://github.com/marcozambi/podfox',
    author='Bastian Reitemeier, Marco Zambianchi',
    author_email='marcozambi@gmail.com',
    license='GPLv3',
    packages=['podfox'],
    zip_safe=False,
    entry_points={
        'console_scripts' : [
            'podfox = podfox.__init__:main'
        ]
    },
    install_requires=[
        'colorama==0.4.6',
        'docopt==0.6.2',
        'feedparser==6.0.11',
        'requests==2.32.3',
        ],
    )
