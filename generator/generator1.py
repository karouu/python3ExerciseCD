# http://www.diveintopython3.net/iterators.html#a-fibonacci-iterator
import re

# Notice function variable scope
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )

'''comprehention, startup cost is high'''
rules = [ build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns ]


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)