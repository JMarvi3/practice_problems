
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def add_pts(pt1, pt2):
    return pt1[0] + pt2[0], pt1[1] + pt2[1]


def count_ships(ships):
    def dfs(start, field: set):
        q = [start]
        while q:
            pt = q.pop()
            for dir in dirs:
                new_pt = add_pts(pt, dir)
                if new_pt in field:
                    q.append(new_pt)
                    field.remove(new_pt)
    field = set()
    for r, row in enumerate(ships):
        for c, cell in enumerate(row):
            if cell == 'S':
                field.add((r, c))
    count = 0
    while field:
        count += 1
        dfs(field.pop(), field)
    return count


ships = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"]
]

print(count_ships(ships))


ships = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"]
]

print(count_ships(ships))

ships = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"],
    [".", ".", ".", "S", "S", ".", ".", "."]
]

print(count_ships(ships))
