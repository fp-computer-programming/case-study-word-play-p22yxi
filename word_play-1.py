# Yongdong Xi Mar 17
with open('words.txt') as infile, open('greater_than_20.txt', 'w') as outfile:
    for line in infile.readlines():
        if len(line) > 20:
            outfile.write(line)

    







    

