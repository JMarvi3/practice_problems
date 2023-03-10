from typing import List
from words import shortest_word


def countries_with_united(countries: List[str]):
    return [country for country in countries if 'united' in country.lower()]


def countries_beginning_and_ending_in_vowel(countries: List[str]):
    vowels = set('aeiou')
    return [country for country in countries if country[0].lower() in vowels
            and country[-1].lower() in vowels]


def countries_with_more_than_half_vowels(countries: List[str]):
    vowels = set('aeiou')
    result = []
    for country in countries:
        vowel_count = sum(c.lower() in vowels for c in country)
        # this is safe floating point because 0.5 is exactly representable in binary
        if vowel_count / len(country) > 0.5:
            result.append(country)
    return result


def shortest_country_name(countries: List[str]):
    return shortest_word(countries)
    # shortest_country, shortest_len = None, float('inf')
    # for country in countries:
    #     if len(country) < shortest_len:
    #         shortest_country = country
    #         shortest_len = len(country)
    # return shortest_country


def countries_with_only_one_vowel(countries: List[str]):
    vowels = set('aeiou')
    len_vowels = len(vowels)
    results = []
    for country in countries:
        number_of_vowels = len_vowels - len(vowels - set(country.lower()))
        if number_of_vowels == 1:
            results.append(country)
    return results


def countries_with_other_country_in_name(countries: List[str]):
    # there are less than 200 countries in the world, so O(n^2) should be acceptable
    results = []
    for country in countries:
        for other_country in countries:
            if country != other_country and other_country.lower() in country.lower():
                # print(f"{country}, {other_country}")
                results.append(country)
                break
    return results


countries = open('countries.txt').read().splitlines()
