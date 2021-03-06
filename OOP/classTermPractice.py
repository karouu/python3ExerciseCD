# python 3 version

import random
import requests
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

PHRASES = {"class %%%(%%%):": "Make a class named %%% that is-a %%%.",

           "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** parameters.",

           "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",

           "*** = %%%()": "Set *** to an instance of class %%%.",

           "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",

           "***.*** = '***'": "From *** get the *** attribute and set it to '***'." }

# do they want to drill phrases first?
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
#print(sys.argv) file directory

# load up the words from the website
text = requests.get(WORD_URL)
WORDS = text.text.splitlines() # a list

def convert(snippet, phrase):
    #list comprehension
    class_names = [w.capitalize() for w in random.sample( WORDS, snippet.count("%%%") )]
    other_names = random.sample( WORDS, snippet.count("***") )
    param_names = []
    results = []

    for i in range(0, snippet.count("@@@")):  #@@@ arg names
        param_count = random.randint(1, 3)
        param_names.append(', '.join( random.sample(WORDS, param_count)) )

    for sentence in (snippet, phrase):  # tuple generator
        result = sentence[:]     # copy

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names:
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
        
    return results

# keep going until they hit CTRL-D
if __name__ == '__main__':
    try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = PHRASES[snippet]

                question, answer = convert(snippet, phrase)  # a , b = [1, 2]

                if PHRASE_FIRST:
                    question, answer = answer, question
                print(question)
                input("> ")
                print( "ANSWER: {}\n\n".format(answer) )
    except EOFError:
        print("\nBye")
