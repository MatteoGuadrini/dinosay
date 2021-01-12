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

COMIC_TYPE = {
    'cartoon': {
        'horizontal_char': 'o',
        'top_sx_char': '0',
        'top_dx_char': '0',
        'bottom_sx_char': 'O',
        'bottom_dx_char': 'O',
        'middle_char': 'o'
    },
    'think': {
        'horizontal_char': '-',
        'top_sx_char': '(',
        'top_dx_char': ')',
        'bottom_sx_char': '(',
        'bottom_dx_char': ')',
        'middle_char': '|'
    },
    'angry': {
        'horizontal_char': '◇',
        'top_sx_char': '<',
        'top_dx_char': '>',
        'bottom_sx_char': '<',
        'bottom_dx_char': '>',
        'middle_char': '◇'
    },
    'star': {
        'horizontal_char': '☆',
        'top_sx_char': '☆',
        'top_dx_char': '☆',
        'bottom_sx_char': '☆',
        'bottom_dx_char': '☆',
        'middle_char': '☆'
    },
    'hungry': {
        'horizontal_char': '-',
        'top_sx_char': '{',
        'top_dx_char': '}',
        'bottom_sx_char': '{',
        'bottom_dx_char': '}',
        'middle_char': '^'
    },
    'math': {
        'horizontal_char': '=',
        'top_sx_char': '+',
        'top_dx_char': '-',
        'bottom_sx_char': '*',
        'bottom_dx_char': '/',
        'middle_char': '%'
    },
    'borg': {
        'horizontal_char': '=',
        'top_sx_char': 'o',
        'top_dx_char': 'o',
        'bottom_sx_char': 'o',
        'bottom_dx_char': 'o',
        'middle_char': '='
    },
    'table': {
        'horizontal_char': '-',
        'top_sx_char': '+',
        'top_dx_char': '+',
        'bottom_sx_char': '+',
        'bottom_dx_char': '+',
        'middle_char': '|'
    },
    'bones': {
        'horizontal_char': '=',
        'top_sx_char': '%',
        'top_dx_char': '%',
        'bottom_sx_char': '%',
        'bottom_dx_char': '%',
        'middle_char': '+'
    },
    'love': {
        'horizontal_char': '♡',
        'top_sx_char': '♡',
        'top_dx_char': '♡',
        'bottom_sx_char': '♡',
        'bottom_dx_char': '♡',
        'middle_char': '♡'
    },
    'scoop': {
        'horizontal_char': '*',
        'top_sx_char': '*',
        'top_dx_char': '*',
        'bottom_sx_char': '*',
        'bottom_dx_char': '*',
        'middle_char': '*'
    }
}

DINO_TYPE = {
    'tyrannosaurus': r"""$comic
                                                 ____
     ___                                      .-~    '.
    `-._~-.                                  / /  ~$eye\   )
         \  \                               | /  \~\.  `\
         ]  |                              /  |  |< ~\(..)
        /   !                        _.--~T   \  \<   .,,
       /   /                 ____.--~ .    _  /~\ \< /
      /   /             .-~~'        /|   /o\ /-~\ \_|
     /   /             /     )      |o|  / /|o/_   '--'
    /   /           .-'(     l__   _j \_/ / /\|~    .
    /    l          /    \       ~~~|    `/ / / \.__/l_
    |     \     _.-'      ~-\__     l      /_/~-.___.--~
    |      ~---~           /   ~~'---\_    __[o,
    l  .                _.    ___     _>-/~
    \  \     .      .-~   .-~   ~>--'  /
     \  ~---'            /         _.-'
      '-.,_____.,_  _.--~\     _.-~
                  ~~     (   _}
                         `. ~(
                           )  \
                     /,`--'~\--'~\
    """,
    'dimetrodon': r"""$comic
                                _._
                              _/:|:
                             /||||||.
                             ||||||||.
                            /|||||||||:
                           /|||||||||||
                          .|||||||||||||
                          | ||||||||||||:
                        _/| |||||||||||||:_=---.._
                        | | |||||:'''':||  '~-._  '-.
                      _/| | ||'         '-._   _:    ;
                      | | | '               '~~     _;
                      | '                _.=._    _-~
                   _.~                  {     '-_'
           _.--=.-~       _.._          {_       }
       _.-~   $eye-,        {    '-._     _. '~==+  |
      ('          }       \_      \_.=~       |  |
      `,,,,,,,'  /_         ~-_    )         <_oo_>
       $tongue `-----~~/ /'===...===' +   /
               <_oo_>         /  //
                             /  //
                            <_oo_>
    """,
    'ankylosaur': r"""$comic
    
                            /~~~~~~~~~~~~\_
       _+=+_             _[~  /~~~~~~~~~~~~\_     
      {''|''}         [~~~    [~   /~~~~~~~~~\_
       ''':-'~[~[~'~[~  ((++     [~  _/~~~~~~~~\_
            '=_   [    ,==, ((++    [    /~~~~~~~\-~~~-.
               ~-_ _=+-(   )/   ((++  .~~~.[~~~~(  {$eye} \`.
                       /   }\ /     (     }     (   .   ''}
                      (  .+   \ /  //     )    / .,  ''''/
                      \\  \     \ (   .+~~\_  /.= /'''''$tongue
                      <'_V_'>      \\  \    ~~~~~~\\  \
                                    \\  \          \\  \
                                    <'_V_'>        <'_V_'>
    """,
    'hypsilophodon': r"""$comic
                                  ___......__             _ 
                              _.-'           ~-_       _.=$eye~~-_
      --=====-.-.-_----------~   .--.       _   -.__.-~ ( ___==>
                    '''--...__  (    \ \\\ { )       _.-~   $tongue
                              =_ ~_  \\-~~~//~~~~-=-~
                               |-=-~_ \\   \\
                               |_/   =. )   ~}
                               |}      ||
                              //       ||
                            _//        {{
                         '='~'          \\_
                                         ~~'
    """,
    'stegosaurus': r"""$comic
    
                            .       .
                           / `.   .' \
                   .---.  <    > <    >  .---.
                   |    \  \ - ~ ~ - /  /    |
                    ~-..-~             ~-..-~
                \~~~\.'                    `./~~~/
                 \__/                        \__/
                  /                  .-    .  \
           _._ _.-    .-~ ~-.       /       }   \/~~~/
       _.-'$eye  }~     /       }     {        ;    \__/
      {'__,  /      (       /      {       /      `. ,~~|   .     .
      $tongue`''''='~~-.__(      /_      |      /- _      `..-'   \\   //
                   / \   =/  ~~--~~{    ./|    ~-.     `-..__\\_//_.-'
                  {   \  +\         \  =\ (        ~ - . _ _ _..---~
                  |  | {   }         \   \_\
                 '---.o___,'       .o___,'
    """,
    'deinonychus': r"""$comic
    
                                                        .--.__
                                                      .~ ($eye)  ~~~---_
                                                     {     `-_~,,,,,,)
                                                     {    (_  ',
                                                      ~    . = _',
                                                       ~-   '.  =-'
                                                         ~     :
      .                                             _,.-~     ('');
      '.                                         .-~        \  \ ;
        ':-_                                _.--~            \  \;      _-=,.
          ~-:-.__                       _.-~                 {  '---- _'-=,.
             ~-._~--._             __.-~                     ~---------=,.`
                 ~~-._~~-----~~~~~~       .+++~~~~~~~~-__   /
                      ~-.,____           {   -     +   }  _/
                              ~~-.______{_    _ -=\ / /_.~
                                   :      ~--~    // /         ..-
                                   :   / /      // /         ((
                                   :  / /      {   `-------,. ))
                                   :   /        ''=--------. }o
                      .=._________,'  )                     ))
                      )  _________ -''                     ~~
                     / /  _ _
                    (_.-.'O'-'.
    """,
    'pterodactyl': r"""$comic
    
                                 <\              _
                                  \\          _/{
                           _       \\       _-   -_
                         /{        / `\   _-     - -_
                       _~  =      ( $eye  \ -        -  -_
                     _- -   ~-_   \( =\ \           -  -_
                   _~  -       ~_ | 1 :\ \      _-~-_ -  -_
                 _-   -          ~  |V: \ \  _-~     ~-_-  -_
              _-~   -            /  | :  \ \            ~-_- -_
           _-~    -   _.._      {   | : _-``               ~- _-_
        _-~   -__..--~    ~-_  {   : \:}
      =~__.--~~              ~-_\  :  /
                                 \ : /__
                                //`Y'--\\
                               <+       \\
                                \\      WWW
                                '
    """,
    'archaeopteryx': r"""$comic
    
                            _
                        __~$eye~_
                        ~~;  ~_
          _             $tongue   ~  ~_                _
         '_\;__._._._._._._]   ~_._._._._._.__;/_`
         '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
         (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
        (/ / / / / | | | ~(/    \) ~ | | \ \ \ \ \)
       (/ / / / /  ~ ~ ~   (/  \)    ~ ~  \ \ \ \ \)
      (/ / / / ~          / (||)|          ~ \ \ \ \)
      ~ / / ~            M  /||\M             ~ \ \ ~
       ~ ~                  /||\                 ~ ~
                           //||\\
                           //||\\
                           //||\\
                           '/||\'
    """,
    'maiasaur': r"""$comic
    
                                         _..-=~=-._
                                    _.-~'          ~.
                        __..---~~~~~                 ~.
                   _.-~~                      _.._     ~.
               _ -~_                         /    \      ;
              ( ` '$eye)                       {      |      :
              /                             |      |      :
             /     /}         (  )          |      |     .-
            /     //-=-~-_-_  |  |          \      ;    .'
           /     //     | =._-|  }/ / / /_.==\     ; _.' 
          ( oo  //      = )  ~| /.__..-='|    \    :' 
           ====||      / /    + )    \   |_.-~`\   :
            $tongue          / /    / /      \  |     ([ ]) 
                     /_/    / /       (  ]     `/ \' 
                    (((|   /_/      __/_/__    -| |--
                          (((|      -----     __|_|__
                           '''                 -----
    """,
    'pleisiosaur': r"""$comic
    
    
                       _..--+~/$eye-~--.
                   _-=~      (  .   '
                _-~     _.--=.\ \''''
              _~      _-       \ \$tongue_\
             =      _=          '--'
            '      =                             .
           :      :       ____                   '=_. ___
      ___  |      ;                            ____ '~--.~.
           ;      ;                               _____  } |
        ___=       \ ___ __     __..-...__           ___/__/__
           :        =_     _.-~~          ~~--.__
      _____ \         ~-+-~                   ___~=_______
           ~@#~~ == ...______ __ ___ _--~~--_
    """,
    'brachiosaur': r"""$comic
    
         _
       .~$eye`,
      {__,  \
      $tongue    \' \
           \  \
            \  \
             \  `._            __.__
              \    ~-._  _.==~~     ~~--.._
               \        '                  ~-.
                \      _-   -_                `.
                 \    /       }        .-    .  \
                  `. |      /  }      (       ;  \
                    `|     /  /       (       :   '\
                     \    |  /        |      /       \
                      |     /`-.______.\     |~-.      \
                      |   |/           (     |   `.      \_
                      |   ||            ~\   \      '._    `-.._____..----..___
                      |   |/             _\   \         ~-.__________.-~~~~~~~~~'''
                    .o'___/            .o______}
    """,
    'corythosaur': r"""$comic
    
                                             .--.
                                            {(~~)}
                           __..._         _.''''$eye`,._
                       _.-'      '~-._.-~~     (  .__}
                    _-~                       _.`--$tongue
                 _-~     _         /~\    _.-~     
              _-~     ,-~ ~-.      \\ ) .~
            .'       {       )      \\|'
          .'         {       /  _.-' |:
        .'            \     /.-'     \\
      .'        __.-~.=\   /          `}
      ;      _.-~   / ./ |  }
      {    _.'     / /   | /
      {    =      {=+__  | :
      :   :_      `-- = \,_`-,.
       `.   '=,_
          '-.___'_::='
    """,
    'parasaurolophus': r"""$comic
    
                _
               //
              //
           __/(
       _.~-$eye  ~-.
      {_____)    `.           _..=~~~~=._
       $tongue     ~-_    \      _.=~           '=.
               \    `._.=~            .=.   :=._
                -         __         (   \   : \)
                 ~.      (  }       (     |   : :
                   `:     \ \        \    |\   ; :
                     \     \ }        \   / |  ;  }
                      `-.__//__.==~~=._\ (_/  ;  ;
                          //           | |/  ;  ;
                         {{       _____|_/ ;   ;
                          `      ---- _=.=`   ~ 
                                  __:='    .='
                              ..:~____.==''
    """,
    'triceratops': r"""$comic
    
                            __.--'~~~~~`--.
         ..       __.    .-~               ~-.
         ((\     /   `}.~                     `.
          \\\  .{     }               /     \   \
      (\   \\~~       }              |       }   \
       \`.-~ -$eye~     }  ,-,.         |       )    \
       (___     ) _}  (    :        |    / /      `._
        $tongue`----._-~.     _\ \ |_       \   / /-.__     `._
               ~~----~~  \ \| ~~--~~~(  + /     ~-._    ~-._
                         /  /         \  \          ~--.,___~_-_.
                      __/  /          _\  )
                    .<___.'         .<___/
    """
}

COLORS = {
    'purple': Template('\033[95m$body\033[0m'),
    'cyan': Template('\033[96m$body\033[0m'),
    'darkcyan': Template('\033[36m$body\033[0m'),
    'blue': Template('\033[94m$body\033[0m'),
    'green': Template('\033[92m$body\033[0m'),
    'yellow': Template('\033[93m$body\033[0m'),
    'red': Template('\033[91m$body\033[0m')
}


# endregion

# region classes
class Dino:
    """
    ASCII dinosaur class
    """

    def __init__(self, body, message=None, behavior=None, color=None):
        """
        ASCII dinosaur object

        :param body: ASCII body of dinosaur
        :param message: message to print
        :param behavior: behavior that determines the value of $ eye, $ tongue and $ comic in the body
        :param color: color of dinosaur. See COLORS dictionary.
        """
        self.body = body
        self.message = message
        self.behavior = behavior
        self.color = color


# endregion

# region functions
def dinoprint(message, body, behavior='normal'):
    """
    Print dinosaur body and message

    :param message: text message
    :param body: dinoaur body
    :param behavior: name of behavior
    :return:
    """
    # Get element on behavior dictionary
    element = behavior_selector(behavior)
    # Create message comic
    comic_type = element.get('comic', {})
    comic = make_comic(message, **comic_type)
    # Print dinosaur
    eyes = element.get('eye')
    tongue = element.get('tongue')
    dinosaur = Template(body)
    print(dinosaur.safe_substitute(
        eye=eyes[0],
        eyes=eyes,
        tongue=tongue if tongue else '',
        comic=comic
    ))


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
        'happy': {'eye': EYE_TYPE.get('happy'), 'comic': COMIC_TYPE.get('cartoon')},
        'joking': {'eye': EYE_TYPE.get('happy'), 'tongue': TONGUE_TYPE.get('classic'),
                   'comic': COMIC_TYPE.get('love')},
        'lazy': {'eye': EYE_TYPE.get('closed'), 'comic': COMIC_TYPE.get('think')},
        'tired': {'eye': EYE_TYPE.get('closed'), 'tongue': TONGUE_TYPE.get('classic'),
                  'comic': COMIC_TYPE.get('think')},
        'angry': {'eye': EYE_TYPE.get('rage'), 'comic': COMIC_TYPE.get('angry')},
        'nerd': {'eye': EYE_TYPE.get('glass'), 'comic': COMIC_TYPE.get('table')},
        'cyborg': {'eye': EYE_TYPE.get('borg'), 'comic': COMIC_TYPE.get('borg')},
        'dead': {'eye': EYE_TYPE.get('ko'), 'tongue': TONGUE_TYPE.get('classic'), 'comic': COMIC_TYPE.get('bones')},
        'trance': {'eye': EYE_TYPE.get('hypno'), 'comic': COMIC_TYPE.get('star')},
        'stoned': {'eye': EYE_TYPE.get('stoned'), 'comic': COMIC_TYPE.get('scoop')}
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
