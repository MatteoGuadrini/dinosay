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
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import wrap
from string import Template

# endregion

# region variables
LOGO = r"""
 _____     __     __   __     ______     ______     ______     __  __   
/\  __-.  /\ \   /\ "-.\ \   /\  __ \   /\  ___\   /\  __ \   /\ \_\ \  
\ \ \/\ \ \ \ \  \ \ \-.  \  \ \ \/\ \  \ \___  \  \ \  __ \  \ \____ \ 
 \ \____-  \ \_\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\ \_\  \/\_____\
  \/____/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/ 
"""

EYE_TYPE = {
    'classic': 'O O',
    'borg': '= =',
    'stoned': '* *',
    'glass': '0-0',
    'hypno': '@ @',
    'rage': '° °',
    'ko': 'x x',
    'happy': '^ ^',
    'closed': '- -'
}

TONGUE_TYPE = {
    'classic': 'U',
    'right': "\_\\",
    'left': "/_/"
}


# endregion

# region functions
def make_comic(text,
               horizontal_char='-',
               top_sx_char='/',
               top_dx_char='\\',
               bottom_sx_char='\\',
               bottom_dx_char='/',
               middle_char='|'):
    """
    Function that creates the comic of the dinosaur

    :param text: text that appears inside the comic
    :param horizontal_char: comic horizontal character
    :param top_sx_char: first character at the top of the comic
    :param top_dx_char: last character at the top of the comic
    :param bottom_sx_char: first character at the bottom of the comic
    :param bottom_dx_char: last character at the bottom of the comic
    :param middle_char: character of the columns, between the first character at the top and bottom
    :return: string
    """
    # Check length of first part of text
    lines = text.splitlines()
    length_line = len(lines[0]) + 2
    # Build comic
    comic = Template("""$top_sx_char$horizontal_char$top_dx_char
$text
$bottom_sx_char$horizontal_char$bottom_dx_char""")
    return comic.safe_substitute(
        top_sx_char=top_sx_char,
        top_dx_char=top_dx_char,
        horizontal_char=horizontal_char * length_line,
        text='\n'.join(["{0} {1} {0}".format(middle_char, line.ljust(len(lines[0]))) for line in lines]),
        bottom_sx_char=bottom_sx_char,
        bottom_dx_char=bottom_dx_char
    )


def behavior_selector(behavior):
    """
    Function that creates the elements (eyes, tongue) to compose the dinosaur

    :param behavior: behavior selected
    :return: dictionary
    """
    BEHAVIOR = {
        'normal': {'eye': EYE_TYPE.get('classic')},
        'happy': {'eye': EYE_TYPE.get('happy')},
        'joking': {'eye': EYE_TYPE.get('happy'), 'tongue': TONGUE_TYPE.get('classic')},
        'lazy': {'eye': EYE_TYPE.get('closed')},
        'tired': {'eye': EYE_TYPE.get('closed'), 'tongue': TONGUE_TYPE.get('classic')},
        'angry': {'eye': EYE_TYPE.get('rage')},
        'nerd': {'eye': EYE_TYPE.get('glass')},
        'cyborg': {'eye': EYE_TYPE.get('borg')},
        'dead': {'eye': EYE_TYPE.get('ko'), 'tongue': TONGUE_TYPE.get('classic')},
        'trance': {'eye': EYE_TYPE.get('hypno')},
        'stoned': {'eye': EYE_TYPE.get('stoned')}
    }
    return BEHAVIOR.get(behavior, BEHAVIOR['normal'])


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
    parser_object = ArgumentParser(prog='dinosay', description='print messages via ASCII dinosaurs',
                                   formatter_class=RawDescriptionHelpFormatter, epilog=LOGO)
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
