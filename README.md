# dinosay

_dinosay_ is a humble, simple, nice and paleolithic alternative to [_cowsay_](https://en.wikipedia.org/wiki/Cowsay).

> The status of this project is: **Work in progress**

```
 _____     __     __   __     ______     ______     ______     __  __   
/\  __-.  /\ \   /\ "-.\ \   /\  __ \   /\  ___\   /\  __ \   /\ \_\ \  
\ \ \/\ \ \ \ \  \ \ \-.  \  \ \ \/\ \  \ \___  \  \ \  __ \  \ \____ \ 
 \ \____-  \ \_\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\ \_\  \/\_____\
  \/____/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/ 
```

## Installation

Unlike its cousin cowsay, _dinosay_ is written in python.

_dinosay_ can be used on the command line or as a python module, to give a dinosaur touch!

```console
$ pip install dinosay
```

## Command line

From the command line, _dinosay_ looks like this:

```console
$ dinosay --help
usage: dinosay [-h] [--version] [-d DINOSAUR | -f FILE | -l] [-c]
               [-b BEHAVIOR] [-i] [-t] [-e EYE] [-w WRAP]
               message
               
print messages via ASCII dinosaurs

positional arguments:
  message               message to print
  
optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
  -d DINOSAUR, --dinosaur DINOSAUR
                        dinosaur to print
  -f FILE, --file FILE  file containing ASCII to print
  -l, --list            list of all dinosaurs and parts
  -c, --color           color dinosaur
  -b BEHAVIOR, --behavior BEHAVIOR
                        behavior of dinosaur
  -i, --idea            idea's speech bubble
  -t, --tongue          shape of the tongue
  -e EYE, --eye EYE     shape of the eye
  -w WRAP, --wrap WRAP  length of the message

```

## Python module

Instead, using it as a python module, we'll do it like this:

```python
from dinosay import dinoprint
msg = "Hi, I'm dinosay!"
dinoprint(msg)
```