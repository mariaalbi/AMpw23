from string import punctuation
def words_count(text: str) -> dict:
    words = text.lower().replace(".", "").replace(",", "").split()
    data = {}
    for word in words:
        if word not in data:
            data[word] = 1
        else:
            data[word] += 1
    return data
text = words_count("this Is is, is a. A a This sentence")
print(text)