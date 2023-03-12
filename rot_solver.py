# american-english: https://manpages.ubuntu.com/manpages/bionic/man5/american-english.5.html
def rot(s: str, shift):
    result = ''
    for c in s:
        if c.islower():
            result += chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
        elif c.isupper():
            result += chr(ord('A') + (ord(c) - ord('A') + shift) % 26)
        else:
            result += c
    return result


def decrypt(s):
    filtered_s = ''.join(c.lower() for c in s if c.isalpha() or c.isspace())
    rots = [rot(filtered_s, shift) for shift in range(26)]
    scores = [sum(word in words for word in r.split()) for r in rots]
    max_shift, max_score = 0, 0
    for shift, score in enumerate(scores):
        if score > max_score:
            max_shift, max_score = shift, score
    return (-max_shift) % 26, rot(s, max_shift)


for i in (1, 2, -1, 27):
    print(i, rot("HELLO", i))
print(rot("Hello, Rick", 1))


words = set(open('american-english').read().splitlines())

print(decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft"))
