class Trie:
    def __init__(self):
        self.children = dict()
        self.term = False

    def add_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.term = True

    def add_words(self, word_list):
        for word in word_list:
            self.add_word(word)


def boggle(grid, word_trie):
    grid_dict = dict()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            grid_dict[(x, y)] = c
    max_x, max_y = x, y
    seen = set()
    for x in range(max_x+1):
        for y in range(max_y+1):
            q = [((x, y), word_trie, [], '')]
            while q:
                pt, node, path, curr_word = q.pop()
                if grid_dict[pt] not in node.children:
                    continue
                path = path + [pt]
                curr_word = curr_word + grid_dict[pt]
                node = node.children[grid_dict[pt]]
                if len(curr_word) >= 3 and node.term and curr_word not in seen:
                    seen.add(curr_word)
                    yield curr_word
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx != 0 or dx != 0:
                            new_pt = pt[0] + dx, pt[1] + dy
                            if new_pt in grid_dict and new_pt not in path:
                                q.append((new_pt, node, path, curr_word))


word_trie = Trie()
word_trie.add_words(open('sowpods.txt').read().splitlines())
for grid in ["BE\nTQ", "ZQQZ\nZAEZ\nZUDZ\nZQQZ", "MSEF\nRATD\nLONE\nKAFB"]:
    print(list(boggle(grid.splitlines(), word_trie)))
