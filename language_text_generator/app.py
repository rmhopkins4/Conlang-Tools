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


def generate_word(syllables: list[str], syllable_selection_dropoff: float, syllable_count_dropoff: float,
                  categories: dict[str, str], character_dropoff: float, rewrite: dict[str, str]):
    # pick a syllable
    def get_syllable_helper(syl: list[str], syllable_dropoff: float):
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
            return get_syllable_helper(syl[1:], syllable_dropoff)

    def syllable_retrieval(syllables: list[str], syllable_dropoff: float):
        syllable = ""
        while not syllable:
            syllable = get_syllable_helper(syllables, syllable_dropoff)
        return syllable

    # would generate infinitely long words! No can do.
    if syllable_count_dropoff == 0:
        return None
    num_syllables = 1
    while random.random() >= syllable_count_dropoff:
        num_syllables += 1

    # get multiple syllables
    syllable_template = "".join([syllable_retrieval(syllables, syllable_selection_dropoff)
                                 for _ in range(num_syllables)])

    # get the characters for each letter in the syllable
    def get_char_helper(characters: str, character_dropoff: float) -> str:
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
            return get_char_helper(characters[1:], character_dropoff)

    def char_retrieval(key, character_dropoff):
        if key not in list(categories.keys()):
            return key
        characters = categories.get(key)

        char = ""
        while not char:
            char = get_char_helper(characters, character_dropoff)
        return char

    word = "".join([char_retrieval(char, character_dropoff)
                   for char in syllable_template])

    # now rewrite
    for target, replacement in rewrite.items():
        word = re.sub(target, replacement, word)
    return word


# user input

categories = {
    "C": "ptkbdg",
    "R": "rl",
    "V": "ieaou",
}
character_dropoff = .30  # how likely you are to select

rewrite_rules = {
    "ki": "či"
}

syllable_types = [
    "CV",
    "V",
    "CRV",
]
syllable_selection_dropoff = .50  # how likely you are to select
# how likely you are to stop at this number of syllables (1 = always one syllable)
syllable_count_dropoff = .50


for i in range(10):
    print(generate_word(syllables=syllable_types,
                        syllable_selection_dropoff=syllable_selection_dropoff,
                        syllable_count_dropoff=syllable_count_dropoff,
                        categories=categories,
                        character_dropoff=character_dropoff,
                        rewrite=rewrite_rules
                        ))


# 75% periods
