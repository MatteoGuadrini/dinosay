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
usage: dinosay [-h] (--dinosaur NAME | --file DINOFILE | --list)
                 [--color COLORNAME] [--behavior BEHAVIOR] [--idea] [--tongue] [--eye EYE]
                 [--wrap INT] [--random] MESSAGE

```

## Python module

Instead, using it as a python module, we'll do it like this:

```python
from dinosay import dinoprint
msg = "Hi, I'm dinosay!"
dinoprint(msg)
```