import re


def __replace_substring_from_category(input_string, target_category, replacement_category, pattern):
    # Same as before, the function that replaces the input_string with new_string based on the pattern
    # add '#' to front and back to handle start and end of string
    input_string = '#' + input_string + '#'
    pattern_prefix, pattern_suffix = pattern.split('_')
    escaped_target = re.escape(target_category)

    # Use positive lookahead to ensure non-overlapping replacements
    pattern_regex = rf'{pattern_prefix}(.)(?={pattern_suffix})'
    print(pattern_regex)

    def repl(match):
        char = match.group(1)
        if char in target_category:
            idx = target_category.index(char)
            # different lengths
            if len(replacement_category) - 1 <= idx:
                return f'{pattern_prefix}{""}{pattern_suffix}'
            return f'{pattern_prefix}{replacement_category[idx]}{pattern_suffix}'
        return match.group(0)

    result = re.sub(pattern_regex, repl, input_string)

    # remove '#' that was added to the start and end of the string
    return result.strip('#')


print(__replace_substring_from_category(input_string="cet",
      target_category="ie", replacement_category="o", pattern="c_"))
