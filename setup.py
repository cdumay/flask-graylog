# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""
from setuptools import setup, find_packages

setup(
    name='flask-graylog',
    version=open('VERSION', 'r').read().strip(),
    description="Flask Graylog client",
    long_description=open('README.md', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='Cedric DUMAY',
    author_email='cedric.dumay@gmail.com',
    url='https://github.com/cdumay/flask-graylog',
    license='Apache License',
    py_modules=['flask_graylog'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
