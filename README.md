# Conlang Tools

I like to design constructed languages, or conlangs, so I made some tools that I could use to help me develop them.

## Language Text Generator

Partially complete, pending premade options, sentence/corpus building, and of course, bug fixes
A version using the console and files as input is on the way, to make sure it is not necessary to open a python editor :)

## Sound Change Applier

Mostly complete, pending thorough testing and continued bug fixes.
A version using the console and files as input is on the way, to make sure it is not necessary to open a python editor :)

The purpose of this tool is to simulate sound changes that would occur over many many years, instantly!
Simply provide words and define sound changes and the program will transform the lexicon.

#### How it Works

Edit the following variables in [app.py](https://github.com/rmhopkins4/Conlang-Tools/blob/main/sound_change_applier/app.py) to use the program.

- `word_list` - list of words which will undergo sound changes. Simple enough.
- `categories` - these act like variables, and can be used in the `word_list` or inside the `sound_changes`. Variables can only be one character long (unless rewrite rules are used).
- `sound_changes` - defines what changes go on. Generally, a sound change looks like: _target->replacement/environment_, where underline _ in environment represents where the substitution occurs.
  - ex: `"b->d/_(a)e"` means that b becomes d when it is before (optionally) 'a' followed by 'e'.
- `rewrite_rules` - globally replaces text in `word_list`, `categories`, and `sound_changes`. Formatted like so: _original: replacement_.
  - ex: `"!front!": "ie"`
  - Where the original is found, it is replaced by the replacement, and afterwards, the original is put back.
  - Allows for multi-character variables in `categories`

#### Options

- `show_input` - Defaults to true. When true, output is formatted like so: output [input]
- `rewrite_on_output` - Defaults to true. When true, output is rewritten back to original. When false, rewriting only goes one way.
- `report_rules` - Defaults to false. When true, prints out what rules apply to which words and where.


## Phonology Creator

To be created – will be used to generate a phonology which can be used in my language text generator, or for any other purposes.
