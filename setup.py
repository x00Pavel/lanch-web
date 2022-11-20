import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='lunch_backend',
    version='0.0',
    description='REST API for parsing menus from restaurants',
    author='Pavel Yadlouski',
    author_email='pavel.yadlouski@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests', 'beautifulsoup4']
)
