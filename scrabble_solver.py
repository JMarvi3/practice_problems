import sys
from collections import Counter


scores = dict(a=1, b=3, c=3, d=2, e=1, f=4, g=2, h=4, i=1, j=8, k=5, l=1, m=3, n=1, o=1, p=3, q=10, r=1, s=1, t=1, u=1,
              v=4, w=4, x=8, y=4, z=10, _=0)


def score_word(word):
    return sum(scores[c] for c in word)


def word_possible(word, rack):
    rack_counter = Counter(rack)
    for c in word:
        if rack_counter[c] == 0:
            return False
        rack_counter[c] -= 1
    return True


rack = sys.argv[1].lower()
scrabble_words = list(map(str.lower, open('sowpods.txt').read().splitlines()))
possible_words = []

for word in scrabble_words:
    if word_possible(word, rack):
        possible_words.append((score_word(word), word))

possible_words.sort(reverse=True)

print(possible_words)
