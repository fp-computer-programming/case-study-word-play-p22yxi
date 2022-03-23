# Yongdong Xi Mar 23
def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


def find_unforbidden_words(file):
    string = input("Enter a string of allowed letters: ")

    total = 0
    with open(file) as infile:
        for line in infile.readlines():
            if avoid(line, string) == True:
                total += 1
    return total

print(find_unforbidden_words('words.txt'))