import requests

from pprint import pprint

TOKEN = '2619421814940190'
URL = 'https://superheroapi.com/api/2619421814940190/search/'


def power_stats(url):
    heroes_name = ['Hulk', 'Captain America', 'Thanos']
    heroes_list = {}
    for name in heroes_name:
        response = requests.get(url + name).json()
        heroes_list[name] = int(response['results'][0]['powerstats']['intelligence'])
    return heroes_list


def strongrer(url):
    heroes_stats = power_stats(url)
    return (max(heroes_stats, key=heroes_stats.get))


if __name__ == '__main__':
    print(strongrer(URL))
