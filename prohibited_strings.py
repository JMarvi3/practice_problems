class Trie:
    subs = {'a': '4', 'e': '3', 'i': '1', 'o': '0'}

    def __init__(self):
        self.children = dict()
        self.term = False

    def add_string(self, s):
        states = [self]
        for c in s.lower():
            new_states = []
            for state in states:
                if c not in state.children:
                    state.children[c] = Trie()
                new_states.append(state.children[c])
                if c in Trie.subs:
                    substition = Trie.subs[c]
                    if substition not in state.children:
                        state.children[substition] = Trie()
                    new_states.append(state.children[substition])
            states = new_states
        for state in states:
            state.term = True

    def contains(self, s):
        states = [self]
        for c in s.lower():
            new_states = []
            for state in states:
                if c in state.children:
                    new_states.append(state.children[c])
                if c in Trie.subs:
                    substition = Trie.subs[c]
                    if substition in state.children:
                        new_states.append(state.children[substition])
            states = new_states
        return any(state.term for state in states)

    def contains_any_string(self, s):
        states = [self]
        for c in s.lower():
            new_states = [self]
            for state in states:
                if state.term:
                    return True
                if c in state.children:
                    new_states.append(state.children[c])
                if c in Trie.subs:
                    substition = Trie.subs[c]
                    if substition in state.children:
                        new_states.append(state.children[substition])
            states = new_states
        return any(state.term for state in states)


def valid_username(prohibited_strings, username):
    t = Trie()
    for s in prohibited_strings:
        t.add_string(s)
    return not t.contains_any_string(username)


print(valid_username(['darn', 'heck'], 'D4RN_y0u_T0_h3ck'))
print(valid_username(['darn', 'heck'], 'bob'))
