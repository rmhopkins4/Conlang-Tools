
class Rewriter():
    def __init__(self, rewrite_rules):
        self.rewrite_rules = rewrite_rules

    def write(self, input_word):
        for key, value in self.rewrite_rules.items():
            if key in input_word:
                input_word = input_word.replace(key, value)
        return input_word

    def unwrite(self, output_word):
        for key, value in self.rewrite_rules.items():
            if value in output_word:
                output_word = output_word.replace(value, key)
        return output_word
