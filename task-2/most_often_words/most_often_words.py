words_count_map = {}

with open("text.txt", 'rt') as text:
    for line in text:
        words = line.split(' ')
        for word in words:
            if word in words_count_map:
                words_count_map[word] += 1
            else:
                words_count_map[word] = 1


print(sorted(words_count_map.items(), key=lambda x: x[1])[::-1])
