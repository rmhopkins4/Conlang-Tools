import random
from collections import Counter
import re

# generate a word
#   pick a syllable
#   for phoneme in syllable
#       pick a letter from category
#   for rule in rewrite rule
#       regex replace in the generated word
#   return word


def _get_syllable_helper(syl: list[str], syllable_dropoff: float):
    if 1 < syllable_dropoff or syllable_dropoff < 0:
        return None
    if len(syl) == 0:
        return None
    random_prob = random.random()
    # if dropoff is 0, do equal probabilities
    if syllable_dropoff == 0:
        return random.choice(syl)
    # do power law dropoff process
    if random_prob < syllable_dropoff:
        return syl[0]
    else:
        return _get_syllable_helper(syl[1:], syllable_dropoff)


def _syllable_retrieval(syllables: list[str], syllable_dropoff: float):
    syllable = ""
    while not syllable:
        syllable = _get_syllable_helper(syllables, syllable_dropoff)
    return syllable


def _get_char_helper(characters: str, character_dropoff: float) -> str:
    if 1 < character_dropoff or character_dropoff < 0:
        return None
    if len(characters) == 0:
        return None
    random_prob = random.random()
    # if dropoff is 0, do equal probabilities
    if character_dropoff == 0:
        return random.choice(characters)
    # do power law dropoff process
    if random_prob < character_dropoff:
        return characters[0]
    else:
        return _get_char_helper(characters[1:], character_dropoff)


def _char_retrieval(key, character_dropoff):
    if key not in list(categories.keys()):
        return key
    characters = categories.get(key)

    char = ""
    while not char:
        char = _get_char_helper(characters, character_dropoff)
    return char


def generate_word(syllables: list[str], syllable_selection_dropoff: float, syllable_count_dropoff: float,
                  categories: dict[str, str], character_dropoff: float, rewrite: dict[str, str]):

    # would generate infinitely long words! No can do.
    if syllable_count_dropoff == 0:
        return None
    num_syllables = 1
    while random.random() >= syllable_count_dropoff:
        num_syllables += 1

    # get multiple syllables
    syllable_template = "".join([_syllable_retrieval(syllables, syllable_selection_dropoff)
                                 for _ in range(num_syllables)])

    # get the characters for each letter in the syllable
    word = "".join([_char_retrieval(char, character_dropoff)
                   for char in syllable_template])

    # now rewrite
    for target, replacement in rewrite.items():
        word = re.sub(target, replacement, word)
    return word


# user input
character_dropoff = .30  # higher -> more likely to pick earlier letters
categories = {  # earlier character -> more likely
    "C": "ptkbdg",
    "R": "rl",
    "V": "ieaou",
}

syllable_selection_dropoff = .50  # higher -> more likely to pick earlier syllables
syllable_types = [  # earlier -> more likely
    "CV",
    "V",
    "CRV",
]

syllable_count_dropoff = .40  # higher -> more likely to pick fewer syllables
syllable_counts = {
    2: 0.4,
    1: 0.2,
    3: 0.2,
    4: 0.1,
    5: 0.05,
    6: 0.05,
}

rewrite_rules = {
    "ki": "či"
}

# generate sentence
standard_sentence = " ".join([generate_word(syllables=syllable_types,
                                            syllable_selection_dropoff=syllable_selection_dropoff,
                                            syllable_count_dropoff=syllable_count_dropoff,
                                            categories=categories,
                                            character_dropoff=character_dropoff,
                                            rewrite=rewrite_rules
                                            ) for _ in range(10)])

print(standard_sentence)
