def parse_nba_finals(lines):
    finals = []
    header = lines[0].split(',')
    for line in lines[1:]:
        line = line.split(',')
        game = dict()
        for i, field in enumerate(line):
            game[header[i]]= field
        finals.append(game)
    return finals


def winner_by_year(nba_finals, year):
    for game in nba_finals:
        if game['Year'] == str(year):
            return game['Winner']


def years_won(nba_finals, team):
    return [game['Year'] for game in nba_finals if game['Winner'] == team]


def never_won(nba_finals):
    winners = set()
    losers = set()
    for game in nba_finals:
        winners.add(game['Winner'])
        losers.add(game['Loser'])
    return list(losers.difference(winners))


def won_mvp_more_than_once(nba_finals):
    count = dict()
    for game in nba_finals:
        mvp = game['MVP']
        if mvp:
            count[mvp] = count.get(mvp, 0) + 1
    mvp_times = dict()
    for mvp, times in count.items():
        if times not in mvp_times:
            mvp_times[times] = []
        mvp_times[times].append(mvp)
    for times in sorted(mvp_times, reverse=True):
        print(f"{times} times: {', '.join(mvp_times[times])}")


nba_finals = parse_nba_finals(open('nba_finals.csv').read().splitlines())
print(winner_by_year(nba_finals, '2019'))
print(years_won(nba_finals, 'Detroit Pistons'))
print(never_won(nba_finals))
won_mvp_more_than_once(nba_finals)
