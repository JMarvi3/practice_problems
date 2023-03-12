closing = dict(['()', '[]', '{}'])


def check_brackets(s):
    stack = []
    for c in s:
        if c in closing:
            stack.append(closing[c])
        else:
            if len(stack) == 0 or stack[-1] != c:
                return False
            stack.pop()
    return len(stack) == 0


print(check_brackets("{[()]}"))
print(check_brackets("{}][()"))
