# Welcome to dinosay
<img src="https://raw.githubusercontent.com/MatteoGuadrini/dinosay/b8f1d9a89cbe6a9c24ee4d58ce95d288536f3eed/img/dinosay.svg" alt="dinosay" title="dinosay" width="300" height="300" />

```console
$ dinosay -d ptero "Hi, I'm dinosay, and you?"

                       
                       /---------------------------\
                       | Hi, I'm dinosay, and you? |
                       \---------------------------/
                             \
                              \
                               \

    
                                 <\              _
                                  \\          _/{
                           _       \\       _-   -_
                         /{        / `\   _-     - -_
                       _~  =      ( O  \ -        -  -_
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
```

_dinosay_ is a nice command line tool, which serves...to make a smile.

<script id="asciicast-387811" src="https://asciinema.org/a/387811.js" async></script>

## Command line usage

_dinosay_ is mainly used on the command line.

### Command flags

| short | long       | description                     | args                                             |
|-------|------------|---------------------------------|--------------------------------------------------|
| -d    | --dinosaur | dinosaur to print               | dinosaur name or alias. see (--list/-l/dinolist) |
| -r    | --random   | random dinosaur to print        |                                                  |
| -f    | --file     | file containing ASCII to print  | path of file ASCII                               |
| -l    | --list     | list of all dinosaurs and parts | see (dinolist)                                   |
| -c    | --color    | color dinosaur                  | color name. see (--list/-l/dinolist)             |
| -b    | --behavior | behavior of dinosaur            | behavior name. see (--list/-l/dinolist)          |
| -i    | --idea     | idea's speech bubble            |                                                  |
| -t    | --tongue   | insert tongue                   |                                                  |
| -e    | --eye      | shape of the eye                | shape name. see (--list/-l/dinolist)             |
| -w    | --wrap     | length of the message           | integer of wrapping message                      |

### List all parts

`dinosay`, it's not the only command. 
To list all parts and components you can use the `--list` flag or directly the` dinolist` command.

```console
$ dinolist

DINOSAY list elements and dinosaurs
===================================

DINOSAURS - ALIAS:          BEHAVIOR:      EYE:                 COLORS: 
- tyrannosaurus - trex      - normal       - classic:  O O      - purple
- dimetrodon - dim          - happy        - borg:     = =      - cyan   
- ankylosaur - anky         - joking       - stoned:   * *      - darkcyan     
- hypsilophodon - hypsi     - lazy         - glass:    0-0      - blue     
- stegosaurus - stego       - tired        - hypno:    @ @      - green     
- deinonychus - deino       - nerd         - rage:     ° °      - yellow     
- pterodactyl - ptero       - cyborg       - ko:       x x      - red     
- archaeopteryx - archa     - dead         - happy:    ^ ^      - default     
- maiasaur - maia           - trance       - closed:   - -     
- pleisiosaur - plei        - stoned
- brachiosaur - brachio
- corythosaur - cory
- parasaurolophus - para
- triceratops - trice
```

## Python module usage

_dinosay_ can be used as an output for your script strings. 
What's wrong with adding a little sympathy to your script?

### dinoprint function

The main function of the _dinosay_ module is **dinoprint**.
This function accepts 3 arguments. 
The first, a message to print. 
The second, is the dinosaur body to print (of course, it can be anything; there is no limit to the imagination). 
The third is optional, and the behavior is specified, that is the shape of the eyes, the language and the comic. 
By default it is set to _normal_. Here is a small example:

```python
from dinosay import dinoprint, DINO_TYPE

dinoprint('Hi dinosay!', DINO_TYPE['tyrannosaurus'])
dinoprint('Hi dinosay!', DINO_TYPE['stegosaurus'], behavior='happy')
```

### Dino class

Another feature of the dinosaur module is to build your own dinosaur (or whatever you want). 
In fact, through the _Dino_ class, we can build a dinosaur object.

```python
from dinosay import dinoprint, Dino
body = r"""
           __n__n__
    .------`-\$eyes/-'
   /  ##  ## (oo)
  / \## __   ./
     |//YY \|/
     |||   |||
"""
my_dino = Dino(body, "Hi, I'm alternative of cowsay", behavior='happy')
dinoprint(my_dino.message, my_dino.body, my_dino.behavior)

# Now in color
my_dino.color = 'red'
my_dino.apply_color()
dinoprint(my_dino.message, my_dino.body, my_dino.behavior)
```

## Acknowledgments

dinosay was born from the minds of two children (my children) who are fond of animals and dinosaurs. 
I thank them for making this tool but also for the wonderful days they gave me together.