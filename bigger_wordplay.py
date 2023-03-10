import time


def double_letter_count(word):
    init = ''
    count = 0
    for c in word:
        if c == init:
            init = ''
            count += 1
        else:
            init = c
    return count


def can_be_made_from_only_letters(word, availableLetters):
    return len(set(word) - set(availableLetters)) == 0


scrabble_words = open('sowpods.txt').read().splitlines()

print(max((word for word in scrabble_words if len(set(word)) == len(word)), key=len))
print([word for word in scrabble_words if len(word) >= 8 and len(set(word)) <= 3])
print([word for word in scrabble_words if double_letter_count(word) >= 3])

abcdef = set('ABCDEF')
print([word for word in scrabble_words if set(word).intersection(abcdef) == abcdef])

start = time.perf_counter()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
possible_chains = sorted((set(alphabet[left:right+1])
                          for left in range(len(alphabet)) for right in range(left+1, len(alphabet))),
                         key=len, reverse=True)

max_chain = ''
max_chain_set = None
for word in scrabble_words:
    word_set = set(word)
    if len(word_set) <= len(max_chain):
        continue
    for chain in possible_chains:
        if len(chain) <= len(max_chain):  # possible_chains are sorted by descending length
            break
        if word_set.intersection(chain) == chain:  # all the letters are used
            max_chain = ''.join(sorted(chain))
            max_chain_set = chain
            break

print("Longest alphabet chain:", max_chain)
max_chain_set
print("Words with that chain:",
      [word for word in scrabble_words if set(word).intersection(max_chain_set) == max_chain_set])
print(f"Time taken: {time.perf_counter() - start}s")

# alphabet_sets = set(map(frozenset, scrabble_words))
# print(len(alphabet_sets), len(scrabble_words))
#
# max_chain = ''
# for left in range(len(alphabet)):
#     for right in range(left+1, len(alphabet)):
#         chain = frozenset(alphabet[left:right+1])
#         if chain in alphabet_sets and len(chain) > len(max_chain):
#             max_chain = alphabet[left:right+1]
# print(max_chain)
# print(frozenset('ABCDEF') in alphabet_sets)

