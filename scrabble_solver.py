import sys
from collections import Counter


scores = dict(a=1, b=3, c=3, d=2, e=1, f=4, g=2, h=4, i=1, j=8, k=5, l=1, m=3, n=1, o=1, p=3, q=10, r=1, s=1, t=1, u=1,
              v=4, w=4, x=8, y=4, z=10, _=0)


def score_word(word, rack):
    word_counter = Counter(word)
    rack_counter = Counter(rack)
    leftover_letters = word_counter - rack_counter
    if rack_counter['_'] != 0:
        if leftover_letters.total() != rack_counter['_']:
            return -1
    elif leftover_letters.total() != 0:
        return -1
    used_letters = word_counter - leftover_letters
    return sum(scores[k]*v for k, v in used_letters.items())


rack = sys.argv[1].lower()
scrabble_words = list(map(str.lower, open('sowpods.txt').read().splitlines()))
possible_words = []

for word in scrabble_words:
    score = score_word(word, rack)
    if score > 0:
        possible_words.append((score, word))


possible_words.sort(reverse=True)

print(possible_words)
