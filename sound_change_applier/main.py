import re

# define categories
categories = {
    "V": "aeiou",
    "C": "ptcqbdgdfmnlrhs",
    "F": "ie",
    "B": "ou",
    "S": "ptc",
    "Z": "bdg",
    "N": "nm"
}


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

    # Use positive lookahead to ensure non-overlapping replacements
    pattern_regex = rf'({(pattern.split("_")[0])}){target}(?={(pattern.split("_")[1])})'

    # replaced by another group
    if "[" in replacement:
        if "[" not in target:
            raise ValueError(
                "Replace element with category")
            result = re.sub(pattern_regex, rf'\1{replacement}', input_string)
        else:
            replacement_list = re.findall(r'\[.*?\]|\S', replacement)

            def __match_func(match):
                return str(rf"{match.group(1)}") + "".join([replacement[target.index(match.group()[0])] if len(replacement) > target.index(match.group()[0]) else replacement if not "[" in replacement else "" for replacement in replacement_list])

            result = re.sub(pattern_regex, __match_func, input_string)
    else:
        result = re.sub(pattern_regex, rf'\1{replacement}', input_string)

    # remove '#' that was added to start and end of string
    return result.strip('#')


def apply_sound_change(input_string, sound_shift, categories={}):
    target, remaining_spec = sound_shift.split('->')
    replacement, pattern = remaining_spec.split('/')

    if not "_" in pattern:
        raise ValueError(
            "'_' must be included after the '/'.\nEx: 'F->B/w_' is a valid sound change.")
    if not target and len(pattern) == 1:
        raise ValueError("Invalid sound change.")

    # expand optional possibilities
    def __expand_options(pattern):
        # Helper function to expand options within parentheses in the pattern
        if '(' not in pattern:
            return pattern

        # Find the first group of options enclosed in parentheses
        match = re.search(r'\(([^()]+)\)', pattern)
        if not match:
            return pattern

        # Expand the options for the first group when it is true and when it's not true
        group_option = match.group(1)
        true_scenario = __expand_options(
            pattern.replace(match.group(), group_option, 1))
        false_scenario = __expand_options(
            pattern.replace(match.group(), '', 1))

        return f'{true_scenario}|{false_scenario}'

    pattern = __expand_options(pattern)

    # Replace the category symbols with their corresponding allowed characters
    for category, characters in categories.items():
        pattern = pattern.replace(category, f'[{characters}]')
        target = target.replace(category, f'[{characters}]')
        replacement = replacement.replace(category, f'[{characters}]')

    pattern = __remove_nested_brackets(pattern)
    return __replace_substring(input_string, target=target, replacement=replacement, pattern=pattern)


# Test the function with bracketed characters in the pattern and categories
input_string = "aa"
sound_change = "a->/_"
try:
    result = apply_sound_change(
        input_string, sound_change, categories)
    print(result)
except Exception as e:
    print("Error has been found:", e)
# NOTE: . is a single wildcard, and .+ is an infinite length wildcard
