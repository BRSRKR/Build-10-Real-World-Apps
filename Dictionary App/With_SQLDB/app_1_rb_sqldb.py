import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
query_list = cursor.execute("SELECT Expression FROM Dictionary")
list_of_words = cursor.fetchall()

new_list = []
for i in list_of_words:
    new_list.append(i[0])


users_key_word = input('What word would you like to look up? ')

#Initial Query
#query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % users_word)
#result = cursor.fetchall()

def thesaurus(key_word):
    key_word = key_word.lower()
    alt_key = key_word.title()
    fixed_key = get_close_matches(key_word, new_list)
    new_str = ""
    if key_word in new_list:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % key_word)
        result = cursor.fetchall()
        for i in result:
            new_str = new_str + "\n-" + i[0]
        return new_str
    elif alt_key in new_list:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % alt_key)
        result = cursor.fetchall()
        for i in result:
            new_str = new_str + "\n-" + i[0]
        return new_str
    elif key_word.upper() in new_list:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % key_word.upper())
        result = cursor.fetchall()
        for i in result:
            new_str = new_str + "\n-" + i[0]
        return new_str
    elif fixed_key != []:
        confirm = "N"
        while confirm == "N":
            confirm = input("Did you mean " + fixed_key[0] + "? Y or N: ").upper()
            if confirm == "N" or confirm == "NO":
                key_word = input("What word would you like to look up? ").lower()
                if key_word in new_list:
                    break
                elif key_word.title() in new_list:
                    key_word = key_word.title()
                    break
                elif key_word.upper() in new_list:
                    key_w(ord = key_word.upper()
                    break
                else:
                    fixed_key = get_close_matches(key_word, new_list)
            else:
                key_word = fixed_key[0]

        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression) = '%s'" % key_word)
        result = cursor.fetchall()
        for i in result:
            new_str = new_str + "\n-" + i[0]
        return new_str
    else:
        return "I can not find this word"



print(thesaurus(users_key_word))