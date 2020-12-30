#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: se ts=4 et syn=python:

# created by: matteo.guadrini
# dinosay -- dinosay
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

"""
Module to print paleolithic comics
"""

# region imports
import dinosay
from argparse import ArgumentParser
from textwrap import wrap


# endregion

# region variables

# endregion

# region functions
def wrap_text(text, width=40):
    """
    Function that splits a string of N characters

    :param text: string text
    :param width: width of string. Default is 40 characters
    :return: string
    """
    return "\n".join(wrap(text, width=width))


def parse_arguments():
    """
    Function that captures the parameters and the arguments in the command line

    :return: parser object
    """
    # Create a principal parser
    parser_object = ArgumentParser(prog='dinosay', description='print messages via ASCII dinosaurs')
    parser_object.add_argument('--version', '-v', action='version', version='%(prog)s ' + dinosay.__version__)
    parser_object.add_argument('message', help='message to print')
    input_group = parser_object.add_mutually_exclusive_group()
    input_group.add_argument('-d', '--dinosaur', help='dinosaur to print', dest='dinosaur')
    input_group.add_argument('-f', '--file', help='file containing ASCII to print', dest='file')
    input_group.add_argument('-l', '--list', help='list of all dinosaurs and parts', dest='list', action='store_true')
    parser_object.add_argument('-c', '--color', help='color dinosaur', dest='color', action='store_true')
    parser_object.add_argument('-b', '--behavior', help='behavior of dinosaur', dest='behavior')
    parser_object.add_argument('-i', '--idea', help="idea's speech bubble", dest='idea', action='store_true')
    parser_object.add_argument('-t', '--tongue', help='shape of the tongue', dest='tongue', action='store_true')
    parser_object.add_argument('-e', '--eye', help='shape of the eye', dest='eye')
    parser_object.add_argument('-w', '--wrap', help='length of the message', dest='wrap', type=int)
    # Return parser object
    return parser_object

# endregion

# region main

# endregion
