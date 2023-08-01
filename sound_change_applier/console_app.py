import os
from manager import apply_sound_changes


def parse_total_input_file(file_path: str):
    word_list = []
    sound_changes = []
    categories = {}
    rewrite_rules = {}
    kwargs = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # make sure line is not whitespace or comment
                line = line.strip()
                if line and not line.startswith("#"):
                    # Process the line here
                    if line.startswith("*"):  # kwarg
                        argument, value = line[1:].split("=")
                        if value == 'True':
                            value = True
                        elif value == 'False':
                            value = False
                        kwargs[argument] = value
                    elif "->" in line:  # sound change
                        sound_changes.append(line)
                    elif "=" in line:  # category
                        variable, values = line.split("=")
                        categories[variable] = values
                    elif "//" in line:  # rewrite rule
                        original, replacement = line.split("//")
                        rewrite_rules[original] = replacement
                    else:
                        word_list.append(line)

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("An error occurred while reading the file")

    return word_list, sound_changes, categories, rewrite_rules, kwargs


word_list, sound_changes, categories, rewrite_rules, kwargs = parse_total_input_file(
    "./materials/example_sound_change_input.txt")

result = apply_sound_changes(word_list,
                             sound_changes,
                             categories,
                             rewrite_rules,
                             **kwargs
                             )
print("Output: ")
for word in result:
    print(word)
