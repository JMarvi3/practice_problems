from words import shortest_word, longest_word
from time import perf_counter

baby_names_2020 = open('baby_names_2020_short.txt').read().splitlines()
baby_names_1880 = open('baby_names_1880_short.txt').read().splitlines()
scrabble_words = open('sowpods.txt').read().splitlines()

print(f"Shortest name in 2020: {shortest_word(baby_names_2020)}")
print(f"Longest name in 2020: {longest_word(baby_names_2020)}")

print('Names that when reversed are scrabble words (list):')

start = perf_counter()

for name in baby_names_2020:
    if name.upper()[::-1] in scrabble_words:
        print(name)

list_time = perf_counter() - start
print(f"Time taken: {list_time}s")

scrabble_word_set = set(scrabble_words)
print('Names that when reversed are scrabble words (set):')

start = perf_counter()

for name in baby_names_2020:
    if name.upper()[::-1] in scrabble_word_set:
        print(name)

set_time = perf_counter() - start
print(f"Time taken: {set_time}s")
print(f"{int(list_time/set_time)}x speedup")

print("Baby names in top 40 both in 1880 and 2020:")
print(list(set(baby_names_1880).intersection(baby_names_2020)))
