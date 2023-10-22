import string
from collections import Counter

with open("example.txt") as file:
    text = file.read()

exclude = {" ", "\n"}.union(set(string.punctuation))

c = Counter("This is a test test test".lower())
for ch, freq in c.most_common():
    if ch not in exclude:
        with open("result.txt", "w") as out_file:
            print(ch, freq, file=out_file)
        break


