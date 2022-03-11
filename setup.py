#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Setup"""
from rename_flac import __version__
from setuptools import setup

setup(
    name='rename-flac',
    version=__version__,
    description="""A command-line tool that takes the information from FLAC
                metadata to batch rename the files according to a filenaming
                scheme.""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Louis-Philippe Véronneau',
    url='https://gitlab.com/baldurmen/rename-flac',
    py_modules = ['rename_flac'],
    entry_points={
        'console_scripts': [
            'rename-flac = rename_flac:main',
        ]
    },
    test_suite="tests",
    license='GPLv3+',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
    ],
)
