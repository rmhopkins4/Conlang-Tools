import re


def __replace_substring(input_string, original, updated, pattern):
    # Same as before, the function that replaces the original_string with new_string based on the pattern
    input_string = '#' + input_string + '#'
    escaped_original = re.escape(original)
    pattern_regex = r'(' + re.escape(pattern.split('_')
                                     [0]) + r')' + escaped_original + r'(' + re.escape(pattern.split('_')[1]) + r')'
    result = re.sub(pattern_regex, r'\1' + updated + r'\2', input_string)
    return result.strip('#')


def apply_sound_change(input_string, sound_shift):
    """
    Interprets the formatted sound_shift string and performs the replacement on the input string.

    Arguments:
    input_string -- The original string where replacements will be made.
    sound_shift -- The replacement specification in the format 'original->new/pattern'.
                        E.g., 'o->i/_n'

    Returns:
    The modified string after performing the replacements.
    """
    # interpret sound_shift notation
    original, remaining_spec = sound_shift.split('->')
    updated, pattern = remaining_spec.split('/')
    # use old replace_substring method
    return __replace_substring(input_string, original=original, updated=updated, pattern=pattern)


# Test the function
input_string = "on"
sound_change = "o->i/#_n"
result = apply_sound_change(input_string, sound_change)
print(result)
