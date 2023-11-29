import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    count = Counter(words)
    return [word for word, _ in count.most_common(3)]


def top_3_words_01(text):
    """
    work with errors
    """
    words = re.findall(r"\b\w[\w']*\b", text.lower())
    count = Counter(words)
    return [word for word, _ in count.most_common(3)]
