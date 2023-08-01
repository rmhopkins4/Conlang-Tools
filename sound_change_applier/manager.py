import processor

__default_categories = {
    "V": "aeiou",
    "L": "āēīōū",
    "C": "ptcqbdgmnlrhs",
    "F": "ie",
    "B": "ou",
    "S": "ptc",
    "Z": "bdg",
    "N": "nm"
}


def apply_sound_changes(word_list: list[str] = ["lector"], sound_changes: list[str] = ["c->i/F_t"], categories: dict[str, str] = __default_categories, rewrite_rules: dict[str, str] = {}, **kwargs) -> list[str]:
    show_input = kwargs.get('show_input', False)
    rewrite_on_output = kwargs.get('rewrite_on_output', True)
    report_rules = kwargs.get('report_rules', False)
    write_to_file = kwargs.get('write_to_file', "").replace('"', '')

    output = []

    # Rewrite sound changes once
    sound_changes = [rewrite(change, rewrite_rules)
                     for change in sound_changes]

    # Rewrite the categories dictionary once
    categories = {rewrite(key, rewrite_rules): rewrite(
        value, rewrite_rules) for key, value in categories.items()}

    # Rewrite word list once
    rewritten_word_list = [rewrite(word, rewrite_rules)
                           for word in word_list]

    def __do_all_changes(word: str) -> str:
        for change in sound_changes:
            old_word = word
            word, change_indices = processor.apply_sound_change(
                word, change, categories)
            if len(change_indices) > 0 and report_rules:
                # location of where old_word and new_word differ
                output.append(
                    f"{change} applies to {old_word} at {change_indices}")
        return word

    new_word_list = [f"{unwrite(__do_all_changes(word), rewrite_rules) if rewrite_on_output else __do_all_changes(word)}{f' [{unwrite(word, rewrite_rules) if rewrite_on_output else word}] ' if show_input else ''}"
                     for word in rewritten_word_list]

    output.append("--Output Lexicon--")
    output.extend(new_word_list)

    if write_to_file:
        try:
            with open(write_to_file, 'w', encoding='utf-8') as file:
                file.writelines([item + '\n' for item in output])

            print(f"Written to file: {write_to_file}")
        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("An error occurred while reading the file")
    return output


def rewrite(s: str, rewrite_rules: dict[str, str]) -> str:
    for key, value in rewrite_rules.items():
        s = s.replace(key, value)
    return s


def unwrite(s: str, rewrite_rules: dict[str, str]) -> str:
    for key, value in rewrite_rules.items():
        s = s.replace(value, key)
    return s
