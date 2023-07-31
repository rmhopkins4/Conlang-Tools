from manager import apply_sound_changes

# user input
rewrite_rules = {
    "!front!": "F",
    "!back!": "B",
    "sh": "ʃ",
}

categories = {
    "!front!": "ie",
    "!back!": "ou",
    "V": "aeiou",
}

word_list = ["be", "bfe", "bce"]

sound_changes = ["b->d/_(a)e"]

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
