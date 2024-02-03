def main():
    book_path = "books/frankenstein.txt"
    text = get_book_data(book_path)
    print("-----------------------------------------")
    print(f"Data report for {book_path}")
    print("-----------------------------------------")
    print (f"The book contains {word_count(text)} words")
    char_data = letter_count(text)
    char_stats = sort_dict(char_data)

    for key in char_stats:
        print(f"The {key[0]} character was found {key[1]} times")


def get_book_data(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return (len(words))

def letter_count(text):
    char_list = init_counters(text)
    for i in text.lower():
         if i in char_list:
            char_list[i] += 1
    return char_list

def init_counters(text):
    characters = []
    text_dictionary = {}
    for i in text:
        if i.isalpha():
            if i.lower() not in characters:
                characters.append(i.lower())
    for i in characters:
        text_dictionary[i] = 0
    return text_dictionary

def sort_dict(dict):
    dict_list = []
    for i in dict:
        dict_list.append((i,dict[i]))

    dict_list.sort(reverse=True,key=lambda a: a[1])
    return dict_list

main()