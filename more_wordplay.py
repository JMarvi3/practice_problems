from words import words_containing_no_letters, words_containg_only_letters, longest_word


def contains_substring(words, substring):
    return [word for word in words if substring in word]


def starts_with(words, prefix):
    return [word for word in words if word.startswith(prefix)]


def has_prefix_suffix_length(words, prefix, suffix, length):
    return [word for word in words if len(word) == length and word.startswith(prefix) and word.endswith(suffix)]


def letter_count(word, letter):
    return sum(c == letter for c in word)


def a_count(word):
    return letter_count(word, 'A')


def frequency(phrase):
    count = dict()
    for c in phrase:
        count[c] = count.get(c, 0) + 1
    return count


scrabble_words = open('sowpods.txt').read().splitlines()

print([word for word in scrabble_words if word.startswith('TH') and word.endswith('TH')])
# I'm assuming the word has to have a U in it.
print(words_containing_no_letters(filter(lambda word: 'U' in word, scrabble_words), 'AEIO'))
print(words_containing_no_letters(filter(lambda word: len(word) == 15 and 'E' in word, scrabble_words), 'AIOU'))
print([word for word in scrabble_words if len(word) == 11 and word.startswith('PRO') and word.endswith('ING')])
rstlne_words = words_containg_only_letters(scrabble_words, 'RSTLNE')
print(rstlne_words)
print(longest_word(rstlne_words))
aeioshrtn_words = words_containing_no_letters(scrabble_words, 'AEIOSHRTN')
print(aeioshrtn_words)
print(longest_word(aeioshrtn_words))
