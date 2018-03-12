# put your code here.
def print_word_count(filename):
    """ Prints the count of each word in the file. """

    word_dict = {}

    textfile = open(filename)

    for line in textfile:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

    textfile.close()

    for word, count in word_dict.items():
        print word, count

print_word_count('twain.txt')
