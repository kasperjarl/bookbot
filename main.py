def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(book_path) # my code
    character_num = num_of_each_character(text)
    list_of_chars = list(character_num.items())
    list_of_chars.sort(reverse=True, key=sort_on)
    nice_report = fun_nice_report(book_path, num_words, list_of_chars)
    return(nice_report) # changed this


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(path): # this function is added - I must be able to do it more efficent tho...
    with open(path) as x:
        words = x.read()
        words = words.split()
        words = len(words)
        return words

def num_of_each_character(text):
    char_dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char.isalpha() == False:
            pass 

        elif char in char_dict.keys():
         
            #print(f"'{char}' is in the char_dict.keys!")
            # get the current value belonging to that key
            new_char_num = char_dict.get(char)

            # add 1 to that value
            new_char_num += 1

            # update the with something that looks like the below:
            char_dict.update({char:new_char_num})
        #   key.value += 1

        elif char not in char_dict.keys():
        #    print(f"'{char}' is not in the char_dict.keys - we should add it!")
            char_dict[f"{char}"] = 1
        #   key.value += 1
        else:
           print(f"'{char}' is not in char_dict and can't be added to char_dict")
    return char_dict

def sort_on(character_num):
    return character_num[1]

def fun_nice_report(book_path, num_words, list_of_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for i in list_of_chars:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")


main()

