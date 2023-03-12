import sys
from collections import Counter


scores = dict(a=1, b=3, c=3, d=2, e=1, f=4, g=2, h=4, i=1, j=8, k=5, l=1, m=3, n=1, o=1, p=3, q=10, r=1, s=1, t=1, u=1,
              v=4, w=4, x=8, y=4, z=10, _=0)


def score_word(word, rack_counter):
    word_counter = Counter(word)
    leftover_letters = word_counter - rack_counter
    if leftover_letters.total() > rack_counter['_']:
        return -1
    used_letters = word_counter - leftover_letters
    return sum(scores[k]*v for k, v in used_letters.items())


rack = sys.argv[1].lower()
rack_counter = Counter(rack)
scrabble_words = list(map(str.lower, open('sowpods.txt').read().splitlines()))
possible_words = []

for word in scrabble_words:
    score = score_word(word, rack_counter)
    if score >= 0:
        possible_words.append((score, word))


possible_words.sort(reverse=True)

print(possible_words)
