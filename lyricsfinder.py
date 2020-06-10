"""
Thanks to https://search.azlyrics.com
"""

import requests
from bs4 import BeautifulSoup

def get_song_list(song_name):
    results = []
    lyric_dic = {}

    try:
        response = requests.get("https://search.azlyrics.com/search.php?q=" + song_name)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.findAll('table', class_='table table-condensed')
        table = tables[-1]
        for lyrics_list in table.find_all("td", class_="visitedlyr"):
            link = lyrics_list.a['href']
            unwanted = lyrics_list.find('small')
            unwanted.extract()
            result = (lyrics_list.text).strip()
            results.append(result)
            lyric_dic[result] = link
    except:
        print('WRONG INPUT')
        exit()
        
    return results, lyric_dic

def get_lyrics(song_index,song_serach_list, song_link_dic):
    lines = []
    try:
        if song_serach_list[song_index] in song_serach_list:
            get_link = song_link_dic.get(song_serach_list[song_index])
            link_response = requests.get(get_link)
            soup_obj = BeautifulSoup(link_response.text, 'html.parser')
            for lyric in soup_obj.findAll('div', attrs={'class': None}):
                lines.append(lyric.get_text().strip())
    except:
        print('WRONG INDEX NUMBER')
        exit()
    return lines

print(' ')
print('** WELCOME TO LYRICS FINDER **')
print(' ')
song_name = input('ENTER SONG NAME: ')
print(' ')

song_serach_list, song_link_dic = get_song_list(song_name)

for songs in song_serach_list:
    print(songs)

print(' ')
song_index = int(input('ENTER SONG INDEX NUMBER. [EX -> 1]: ')) - 1
print(' ')

lyrics = get_lyrics(song_index,song_serach_list,song_link_dic)

for lyric in lyrics:
    print(lyric)


