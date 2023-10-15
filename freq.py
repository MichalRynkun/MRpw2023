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
