from words import words_containing_no_letters, words_containing_all_letters


def words_containing_UU(words):
    results = []
    for word in words:
        if 'UU' in word:
            results.append(word)
    return results


def words_containing_X_and_Y_and_Z(words):
    return words_containing_all_letters(words, 'XYZ')


def words_containing_Q_but_not_U(words):
    results = []
    for word in words:
        if 'Q' in word and 'U' not in word:
            results.append(word)
    return results


def words_containing_CAT_and_5_length(words):
    results = []
    for word in words:
        if len(word) == 5 and 'CAT' in word:
            results.append(word)
    return results


def words_containing_no_E_or_A_length_at_least_15(words):
    return [word for word in words_containing_no_letters(words, 'EA') if len(word) >= 15]


def words_containing_B_and_X_length_less_than_5(words):
    return [word for word in words_containing_all_letters(words, 'BX') if len(word) < 5]


def words_starting_and_ending_in_Y(words):
    results = []
    for word in words:
        if word[0] == 'Y' and word[-1] == 'Y':
            results.append(word)
    return results


def words_containing_no_vowels(words):
    return words_containing_no_letters(words, 'AEIOUY')


def words_containing_all_vowels(words):
    return words_containing_all_letters(words, 'AEIOU')


def words_containing_all_vowels_in_order(words):
    vowels = 'AEIOU'
    results = []
    for word in words:
        pos = 0
        for c in word:
            if c == vowels[pos]:
                pos += 1
                if pos == len(vowels):
                    results.append(word)
                    break
    return results


def count_words_containing_TYPE(words):
    count = 0
    for word in words:
        if 'TYPE' in word:
            count += 1
    return count


def words_ending_in_GHTLY(words):
    results = []
    for word in words:
        if word.endswith('GHTLY'):
            results.append(word)
    return results


def shortest_word_containing_all_vowels(words):
    words_with_all_vowels = words_containing_all_vowels(words)
    shortest = words_with_all_vowels[0]
    for word in words_with_all_vowels:
        if len(word) < len(shortest):
            shortest = word
    return shortest


def least_common_letter(words):
    counter = dict()
    for word in words:
        for c in word:
            counter[c] = counter.get(c, 0) + 1
    least_count = float('inf')
    for letter in 'QXZ':
        if counter[letter] < least_count:
            least_letter, least_count = letter, counter[letter]
    return least_letter


def is_palindrome(word):
    l, r = 0, len(word)-1
    while l < r:
        if word[l] != word[r]:
            return False
        l, r = l+1, r-1
    return True


def longest_palindrome(words):
    longest_len = 0
    for word in words:
        if len(word) > longest_len and is_palindrome(word):
            longest_len, longest = len(word), word
    return longest


def non_repeated_letters(words):
    not_repeated = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for word in words:
        for i, c in enumerate(word):
            if i != 0 and c == word[i-1]:
                not_repeated.discard(c)
    return list(not_repeated)


words = open('sowpods.txt').read().splitlines()
