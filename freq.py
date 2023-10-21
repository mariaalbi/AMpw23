from string import punctuation
from collections import defaultdict

def words_count(text: str) -> dict:
    lower_text = text.lower()
    for ch in punctuation:
        lower_text = lower_text.replace(ch, "")

    data = defaultdict(int)
    for word in lower_text.split():
        data[word] += 1
    return data

text = words_count("this Is is, is a. A a! This sentence")
print(text)

s = {1, 2, 3}
print(s.pop())
s = {4, 1, 2, 3}
print(s.pop())
s = {4, 5, 0, 1, 2, 3}
print(s.pop())
s = {10, -1, 4, 5, 0, 1, 2, 3}
print(s.pop())
e = set()
print(e)
print(s)
b = {10, 1, 2, 3}
print(b.pop())
d = 10 in b
print(d)
f = 9 in b
print(f)