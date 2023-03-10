import csv

hot_100 = list(csv.DictReader(open('billboard100_2000.csv')))

all_number_ones = set()
weeks_number_one_count = dict()
artist_count = dict()
songs_by_artist = dict()
weeks_count = dict()

for song in hot_100:
    title, artist = song['song'], song['artist']
    song_str = f'"{title}" - {artist}'
    if song['rank'] == '1':
        all_number_ones.add(song_str)
        weeks_number_one_count[song_str] = weeks_number_one_count.get(song_str, 0) + 1
    weeks_count[song_str] = weeks_count.get(song_str, 0) + 1
    artist_count[artist] = artist_count.get(artist, 0) + 1
    songs_by_artist[artist] = songs_by_artist.get(artist, set()).union([f'"{title}"'])

print(', '.join(all_number_ones))
print("Most weeks at #1:", max(weeks_number_one_count, key=lambda song: weeks_number_one_count[song]))
most_ranked_artist = max(artist_count, key=lambda artist: artist_count[artist])
print("Artist with most songs:", most_ranked_artist, "performing:", ', '.join(songs_by_artist[most_ranked_artist]))
most_weeks = max(weeks_count.values())
print("Songs on the charts for the most weeks:",
      ', '.join(song for song in weeks_count if weeks_count[song] == most_weeks))

