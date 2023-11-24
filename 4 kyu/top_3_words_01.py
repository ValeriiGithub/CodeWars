import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    count = Counter(words)
    return [word for word, _ in count.most_common(3)]
