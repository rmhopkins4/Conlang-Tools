import re


def __remove_nested_brackets(str: str):
    output_str = ""
    bracket_depth = 0
    for char in str:
        if char == '[':
            bracket_depth += 1
        if bracket_depth <= 1 or (char != '[' and char != ']'):
            output_str += char
        if char == ']':
            bracket_depth -= 1
    return output_str


def __replace_substring(input_string, target, replacement, pattern):
    # Same as before, the function that replaces the original_string with new_string based on the pattern
    # add '#' to front and back to handle start and end of string
    input_string = '#' + input_string + '#'

    # handle replacement as a list

    # Use positive lookahead and lookbehind to ensure non-overlapping replacements
    pattern_regex = rf'(?<={(pattern.split("_")[0])}){target}(?={(pattern.split("_")[1])})'

    # replaced by another group
    if "[" in replacement:
        if "[" not in target:
            raise ValueError(
                "Replace element with category")
            result = re.sub(pattern_regex, rf'\1{replacement}', input_string)
        else:
            replacement_list = re.findall(r'\[.*?\]|\S', replacement)

            def __match_func(match):
                return "".join([replacement[target.index(match.group()[0])] if len(replacement) > target.index(match.group()[0]) else replacement if not "[" in replacement else "" for replacement in replacement_list])
            result = re.sub(pattern_regex, __match_func, input_string)
    else:
        result = re.sub(pattern_regex, replacement, input_string)

    # remove '#' that was added to start and end of string
    return result.strip('#')


def apply_sound_change(input_string: str = "lector",
                       sound_shift: str = "c->i/F_t",
                       categories: dict[str, str] = {}) -> tuple[str, bool]:
    """Simulates a sound change on a string

    Args:
        input_string (str): Word/morpheme undergoing the sound change
        sound_shift (str): Sound change written in format: (target)->(replacement)_/#_#
        categories (dict, optional): Categories act like variables. They can be used in any position of the sound change. Defaults to {}.

    Raises:
        ValueError: Sound change is invalid

    Returns:
        str: input string after undergoing the sound shift
        bool: whether or not a change has occurred
    """
    target, remaining_spec = sound_shift.split('->')
    replacement, pattern = remaining_spec.split('/')

    if not "_" in pattern:
        raise ValueError(
            "'_' must be included after the '/'.\nEx: 'F->B/w_' is a valid sound change.")
    if not target and len(pattern) == 1:
        raise ValueError("Invalid sound change.")
    if '(' in replacement or ')' in replacement:
        raise ValueError("Optional phonemes are not allowed in replacement.")

    # optional parts are handled by regex with (a)?
    def __add_question_mark_after_closing_parenthesis(sentence):
        modified_sentence = ""
        for char in sentence:
            if char == ')':
                modified_sentence += char + "?"
            else:
                modified_sentence += char
        return modified_sentence

    pattern = __add_question_mark_after_closing_parenthesis(pattern)
    target = __add_question_mark_after_closing_parenthesis(target)

    # Replace the category symbols with their corresponding allowed characters
    for category, characters in categories.items():
        pattern = pattern.replace(category, f'[{characters}]')
        target = target.replace(category, f'[{characters}]')
        replacement = replacement.replace(category, f'[{characters}]')

    pattern = __remove_nested_brackets(pattern)
    replaced = __replace_substring(
        input_string, target=target, replacement=replacement, pattern=pattern)
    return replaced, replaced != input_string


# NOTE: format of sound change is (target)->(replacement)/(environment with '_')
# NOTE: . is a single wildcard and .+ is an infinite length wildcard


if __name__ == "__main__":

    # define categories
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

    # Test the function with bracketed characters in the pattern and categories
    input_string = "bfe"
    sound_change = "b(f)e->d/_"
    result = apply_sound_change(
        input_string, sound_change, __default_categories)
    print(result)
