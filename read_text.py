# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    return content


def count_words():
    text = read_file_content("./story.txt")

    # dictionary to hold 'key:value' of words
    words_dictionary = {}

    # converting the string into a list
    text_to_list = text.split()
    # returning {word:number_of_occurence}
    for word in text_to_list:
        words_dictionary[word] = text_to_list.count(word)

    return words_dictionary


words_dictionary = count_words()
print(words_dictionary)
