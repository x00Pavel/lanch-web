import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='flask_lunch_web',
    version='0.0',
    description='REST API for parsing menus from restaurants',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Pavel Yadlouski',
    author_email='pavel.yadlouski@gmail.com',
    url='',
    keywords='web flask restful api',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
)
