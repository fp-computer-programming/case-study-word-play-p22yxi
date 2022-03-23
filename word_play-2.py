def no_e(word):
    if "e" not in word:
        return True

with open("words.txt") as infile, open("words_without_e.txt", 'w') as outfile:
    for line in infile.readlines():
        if no_e(line) == True:
            outfile.write(line)


def readline_count(file):
    return len(open(file).readlines())



length_all = readline_count("words.txt")
length_no_e = readline_count("words_without_e.txt")
percent_of_no_e_words = (length_no_e / length_all) * 100
print(percent_of_no_e_words,'% words do not have e')
