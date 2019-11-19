#Sci-Fi Ship name generator
#Cameron McDrury 2019
#Takes text files of words with one word to a line. 
#Credit to ashley-bovan.co.uk for the word lists. 

import random

FORMATS = {"adx-noun": "{} {}", "noun-of-noun": "{} of {}", "verb-of-the-noun": "{} of the {}", "the-verb-of-noun": "The {} of {}", "the-number-noun": "The {} {}"}


def get_list_from_file(filename):
    """Takes a txt filename and builds a python list from it."""
    file = open(filename)
    lines = file.readlines()
    file.close()
    word_list = []
    words = []
    
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        words.append(lines[i])
    
    return words
        
        
def generate_name(user_format, nouns, verbs, adverbs, adjectives):
    """Puts random words together and makes a name"""
    if user_format not in FORMATS:
        print("Sorry, invalid format")
        main()
    template = FORMATS[user_format]
    print(template)
    
    noun1 = nouns[random.randint(0, len(nouns))]
    noun2 = nouns[random.randint(0, len(nouns))]
    noun = nouns[random.randint(0, len(nouns))]
    verb = verbs[random.randint(0, len(verbs))]
    adverb = adverbs[random.randint(0, len(adverbs))]
    adjective = adjectives[random.randint(0, len(adjectives))]
    
    name = "ERROR"
    number = -1
    
    if user_format == "adx-noun":
        x = random.randint(0, 1)
        if x == 0:
            name = FORMATS[user_format].format(adverb, noun)
        elif x == 1:
            name = FORMATS[user_format].format(adjective, noun)
    
    elif user_format == "noun-of-noun":
        name = FORMATS[user_format].format(noun1, noun2)
        
    elif user_format == "verb-of-the-noun":
        name = FORMATS[user_format].format(verb, noun)
        
    elif user_format == "the-verb-of-noun":
        name = FORMATS[user_format].format(verb, noun)
        
    elif user_format == "the-number-noun":
        number = random.randint(0, 100)
        name = FORMATS[user_format].format(number, noun)        
    
    print("-"*20)
    print(name)
    print("-"*20)
    main()
    

def main():
    """Main function, organises everything else"""
    verbs = get_list_from_file('31K verbs.txt')
    nouns = get_list_from_file('91K nouns.txt')
    adjectives = get_list_from_file('28K adjectives.txt')
    adverbs = get_list_from_file('6K adverbs.txt') 
    user_format = input('''Chose a format:
    adx-noun
    noun-of-noun
    verb-of-the-noun
    the-verb-of-noun
    the-number-noun
    
    ''').lower()
    
    generate_name(user_format, nouns, verbs, adverbs, adjectives)
    
main()