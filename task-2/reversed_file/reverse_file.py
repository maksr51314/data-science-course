with open("text.txt", 'rt') as file:
    with open("text_reversed.txt", 'wt') as file_reversed:
        for line in reversed(list(file)):
            file_reversed.write(line)