from manager import apply_sound_changes

# These allow global substitutions to input and output.
# Most importantly, this lets you use digraphs in categories, as either variables or as defined values
rewrite_rules = {
    "!front!": "F",
    "!back!": "B",
    "sh": "ʃ",
}

# Variables can only be one character long, (unless defined with rewrite rules).
categories = {
    "!front!": "ie",
    "!back!": "ou",
    "V": "aeiou",
}

#
word_list = [
    "be",
    "bfe",
    "bce",
]

# A sound change looks like: target->replacement/environment.
# The environment must contain an underline _, representing the part that changes.
# Rules apply in the order they are written.
sound_changes = [
    "b->d/_(a)e",
]

result = apply_sound_changes(word_list,
                             sound_changes,
                             categories,
                             rewrite_rules,
                             show_input=True,
                             rewrite_on_output=True,
                             report_rules=False,
                             )
for word in result:
    print(word)
