# -*- coding: utf-8 -*-
""""""

from setuptools import setup, find_packages

setup(
    name='noodle.crawler',
    version='0.1',
    author='',
    author_email='',
    url='https://github.com/noodle-ng/noodle.crawler/',
    license='',
    description='Noodle NG Crawler',
    long_description=open('README.md').read(),
    install_requires=[
        'noodle.core',
        ],
    packages=find_packages(exclude=['tests']),
    namespace_packages=['noodle'],
)