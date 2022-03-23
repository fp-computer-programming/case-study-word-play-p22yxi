# Yongdong Xi
def uses_only(word, available):
    for letter in word:
        if letter not in available:
           return False
    return True


string = input("Enter a string of allowed letters: ")


with open('words.txt') as infile:
    words = []
    for line in infile.readlines():
        if uses_only(line, string) == True:
               words.append(line)
    print(words)