import json
from difflib import get_close_matches

data = json.load(open("data.json"))
user_key_word = input("What word would you like to look up? ")


def thesaurus(key_word):
    key_word = key_word.lower()
    alt_key = key_word.title()
    fixed_key = get_close_matches(key_word, data.keys())
    new_str = ""
    if key_word in data.keys():
        for i in data[key_word]:
            new_str = new_str + "\n-" + i
        return new_str
    elif alt_key in data.keys():
        for i in data[alt_key]:
            new_str = new_str + "\n-" + i
        return new_str
    elif key_word.upper() in data.keys():
        for i in data[key_word.upper()]:
            new_str = new_str + "\n-" + i
        return new_str
    elif fixed_key != []:
        confirm = "N"
        while confirm == "N":
            confirm = input("Did you mean " + fixed_key[0] + "? Y or N: ").upper()
            if confirm == "N" or confirm == "NO":
                key_word = input("What word would you like to look up? ").lower()
                if key_word in data.keys():
                    break
                elif key_word.title() in data.keys():
                    fixed_key = get_close_matches(key_word.title(), data.keys())
                    break
                elif key_word.upper() in data.keys():
                    fixed_key = get_close_matches(key_word.upper(), data.keys())
                    break
                else:
                    fixed_key = get_close_matches(key_word, data.keys())
        for i in data[fixed_key[0]]:
            new_str = new_str + "\n-" + i
        return new_str
    else:
        return "I can not find this word"


print(thesaurus(user_key_word))
