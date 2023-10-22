import string
from collections import Counter
#
#
# c = Counter("This is a test test test".lower())
# print(c.most_common(1))

with open("main.py") as in_file:
    text = in_file.read()

exclude = {"\n", " "}.union(set(string.punctuation))

c = Counter(text.lower())
for ch, freq in c.most_common():
    if ch not in exclude:
        with open("reslt.txt", "w") as out_file:
            print(ch,freq, file=out_file)
        break
