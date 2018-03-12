from sys import argv
from collections import Counter
from string import punctuation

if len(argv) < 2:
    input_file = "test.txt"
else:
    input_file = argv[1]
# put your code here.


# def print_word_count(filename):
#     """ Prints the count of each word in the file. """

#     word_dict = {}
#     punctuation = "!@#$%^&*()_+=-,./?><\\|{}][;:'\""

#     textfile = open(filename)

#     for line in textfile:
#         line = line.strip()
#         words = line.split(" ")
#         for word in words:
#             word = word.strip(punctuation).lower()
#             word_dict[word] = word_dict.get(word, 0) + 1

#     textfile.close()

#     for word, count in word_dict.items():
#         print word, count

#     print len(word_dict)


def print_word_count(filename):
    """ Prints the count of each word in the file. """

    textfile = open(filename)

    file_string = textfile.read()
    words = file_string.split()

    words = [word.strip(punctuation).lower() for word in words]
    word_count = Counter(words)

    textfile.close()

    # alpha_list = sorted(word_count.keys())

    # for word in alpha_list:
    #     print word, word_count[word]

    item_list = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in item_list:
        print word, count

print_word_count(input_file)
