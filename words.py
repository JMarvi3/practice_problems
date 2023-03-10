def words_containing_all_letters(words, letters):
    letters = set(letters)
    return [word for word in words if len(letters - set(word)) == 0]


def words_containing_no_letters(words, letters):
    letters = set(letters)
    result = []
    for word in words:
        for c in word:
            if c in letters:
                break
        else:
            result.append(word)
    return result


def words_containg_only_letters(words, letters):
    letters = set(letters)
    return [word for word in words if not (set(word) - letters)]


def longest_word(words):
    longest, longest_len = None, -float('inf')
    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
            longest = word
    return longest


def shortest_word(words):
    shortest, shortest_len = None, float('inf')
    for word in words:
        if len(word) < shortest_len:
            shortest_len = len(word)
            shortest = word
    return shortest
