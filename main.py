def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num = num_of_words(book_path) # my code
    print(num) # changed this from (text) to (num)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(path): # this function is added - I must be able to do it more efficent tho...
    with open(path) as x:
        words = x.read()
        words = words.split()
        words = len(words)
        return words


main()

