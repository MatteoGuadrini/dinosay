#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# setup -- dinosay
#
#     Copyright (C) 2020 Matteo Guadrini <matteo.guadrini@hotmail.it>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from dinosay import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dinosay',
    version=__version__,
    packages=['dinosay'],
    url='https://github.com/MatteoGuadrini/dinosay',
    project_urls={
        'Documentation': 'https://matteoguadrini.github.io/dinosay',
        'GitHub Project': 'https://github.com/MatteoGuadrini/dinosay',
        'Issue Tracker': 'https://github.com/MatteoGuadrini/dinosay/issues'
    },
    license='GNU General Public License v3.0',
    author='Matteo Guadrini',
    author_email='matteo.guadrini@hotmail.it',
    maintainer='Matteo Guadrini',
    maintainer_email='matteo.guadrini@hotmail.it',
    description='dinosay is a humble, simple, nice and paleolithic alternative to cowsay',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent"
        ],
    entry_points={
        'console_scripts': [
            'dinosay = dinosay.dinosay:dinospeak',
            'dinolist = dinosay.dinosay:dinolist'
        ]
    },
    python_requires='>=3.5'
)
