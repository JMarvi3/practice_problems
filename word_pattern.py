def matches(pattern, input_string):
    pattern_words = dict()
    words = input_string.split()
    if len(words) != len(pattern):
        return False
    for i, c in enumerate(pattern):
        if c not in pattern_words:
            pattern_words[c] = words[i]
        elif pattern_words[c] != words[i]:
            return False
    return True


def matches_part2(pattern, input_string, pattern_words=dict()):
    if len(pattern) == 0:
        return len(input_string) == 0
    c = pattern[0]
    if c in pattern_words:
        c_word = pattern_words[c]
        if not input_string.startswith(pattern_words[c]):
            return False
        return matches_part2(pattern[1:], input_string[len(c_word):], pattern_words)
    for length in range(1, len(input_string) - len(pattern) + 1):
        c_word, rest = input_string[:length], input_string[length:]
        if matches_part2(pattern[1:], rest, {**pattern_words, c: c_word}):
            return True
    return False


print('part1:')
print(matches('abba', 'red blue blue red'))
print(matches('abcabc', 'red blue green red blue green'))
print(matches('abba', 'red blue green red'))

print('part2:')
print(matches_part2('abcba', 'redbluegreenbluered'))
print(matches_part2('aba', 'xxyyyxx'))
print(matches('abba', 'redbluegreenred'))
