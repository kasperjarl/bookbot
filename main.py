def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(book_path) # my code
    character_num = num_of_each_character(text)
    print(num_of_each_character) # changed this from (text) to (num)


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
        if char == " ": # we still have an issue with something that looks like new line
            print("Space detected- skipping")

        elif char in char_dict.keys():
         
            print(f"'{char}' is in the char_dict.keys!")
        #   key.value += 1

        elif char not in char_dict.keys():
            print(f"'{char}' is not in the char_dict.keys - we should add it!")
            char_dict[f"{char}"] = 1
        #   key.value += 1
        # else:
        #   print(f"'{char}' is not in char_dict and can't be added to char_dict")

main()

