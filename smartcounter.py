import string
from collections import Counter

class SmartCounter:

    def __init__(self, file_path):
        self.file_path = file_path

    def _retrieve_text(self):
        exclude = list(string.punctuation)
        with open(self.file_path) as f:
            text = f.read().lower().replace("\n", "")
        for ch in exclude:
            text = text.replace(ch, "")
        return text


    def common_words(self, n=3):
        text = self._retrieve_text()
        counter = Counter(text.split())
        return counter.most_common(n)


    def common_letters(self, n=3):
        text = self._retrieve_text()
        text = text.replace(" ", "")
        counter = Counter(text)
        return counter.most_common(n)

smartr_counter = SmartCounter("class.py")
print(smartr_counter.common_words())
print(smartr_counter.common_letters())