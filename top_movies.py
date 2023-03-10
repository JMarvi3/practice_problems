import csv

top_movies = list(csv.DictReader(open('top_movies.csv')))

print("DreamWorks movies:")
print([movie['Title'] for movie in top_movies if movie['Distributor'] == 'DreamWorks'])
universal_pictures_by_us_sales = sorted((movie for movie in top_movies if movie['Distributor'] == 'Universal Pictures'),
                                        key=lambda movie: movie['US Sales'])
print("Highest grossing movie from Universal Pictures, domestically:")
print(universal_pictures_by_us_sales[-1]['Title'])

earliest_year = min(movie['Release Date'] for movie in top_movies)
print(f"Films from {earliest_year}: "
      f"{', '.join(movie['Title'] for movie in top_movies if movie['Release Date'] == earliest_year)}")

ratings_count = dict()
for movie in top_movies:
    rating = movie['Rating']
    ratings_count[rating] = ratings_count.get(rating, 0) + 1

print("Distribution of ratings:", ratings_count)


