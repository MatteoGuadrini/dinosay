# dinosay

_dinosay_ is a humble, simple, nice and paleolithic alternative to [_cowsay_](https://en.wikipedia.org/wiki/Cowsay).

> The status of this project is: **Work in progress: _alpha_ version**

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
usage: dinosay [-h] [--version] [-d DINOSAUR | -f FILE | -l] [-c COLOR] [-b BEHAVIOR] [-i] [-t] [-e EYE] [-w WRAP] message

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
  -c COLOR, --color COLOR
                        color dinosaur
  -b BEHAVIOR, --behavior BEHAVIOR
                        behavior of dinosaur
  -i, --idea            idea's speech bubble
  -t, --tongue          shape of the tongue
  -e EYE, --eye EYE     shape of the eye
  -w WRAP, --wrap WRAP  length of the message

 _____     __     __   __     ______     ______     ______     __  __   
/\  __-.  /\ \   /\ "-.\ \   /\  __ \   /\  ___\   /\  __ \   /\ \_\ \  
\ \ \/\ \ \ \ \  \ \ \-.  \  \ \ \/\ \  \ \___  \  \ \  __ \  \ \____ \ 
 \ \____-  \ \_\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\ \_\  \/\_____\
  \/____/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/ 
```

## Python module

Instead, using it as a python module, we'll do it like this:

```python
from dinosay.dinosay import dinoprint, DINO_TYPE
msg = "Hi, I'm dinosay!"
dinoprint(msg, DINO_TYPE['tyrannosaurus'])
```

## Open source
_dinosay_ is a open source project. Any contribute, It's welcome.

**A great thanks**.

For donations, press this

For me

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/guos)

For [Telethon](http://www.telethon.it/)

The Telethon Foundation is a non-profit organization recognized by the Ministry of University and Scientific and Technological Research.
They were born in 1990 to respond to the appeal of patients suffering from rare diseases.
Come today, we are organized to dare to listen to them and answers, every day of the year.

<a href="https://www.telethon.it/sostienici/dona-ora"> <img src="https://www.telethon.it/dev/_nuxt/img/c6d474e.svg" alt="Telethon" title="Telethon" width="200" height="104" /> </a>

[Adopt the future](https://www.ioadottoilfuturo.it/)


## Acknowledgments

Thanks to Mark Lutz for writing the _Learning Python_ and _Programming Python_ books that make up my python foundation.

Thanks to Kenneth Reitz and Tanya Schlusser for writing the _The Hitchhiker’s Guide to Python_ books.

Thanks to Dane Hillard for writing the _Practices of the Python Pro_ books.

Special thanks go to my wife, who understood the hours of absence for this development. 
Thanks to my children, for the daily inspiration they give me and to make me realize, that life must be simple.

Thanks Python!