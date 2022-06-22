

import requests
from bs4 import BeautifulSoup
import copy


print(
    "Hi, here is a list of countries you can choose from\n to see top songs of apple music in each of them\n Global, Ukraine, USA, UK, Canada, Mexico, Australia, Japan,\n Spain, France, Germany, South Korea, Armenia, Austria, Costa Rica"
)

oo=True
oo1=True

url_dict = {
    "ukraine": "https://music.apple.com/ae/playlist/top-100-ukraine/pl.815f78effb3844909a8259d759ecbddb",
    "global": "https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31",
    "usa": "https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12",
    "uk": "https://music.apple.com/us/playlist/top-100-uk/pl.c2273b7e89b44121b3093f67228918e7",
    "canada": "https://music.apple.com/us/playlist/top-100-canada/pl.79bac9045a2540e0b195e983df8ba569",
    "mexico": "https://music.apple.com/us/playlist/top-100-mexico/pl.df3f10ca27b1479087de2cd3f9f6716b",
    "australia": "https://music.apple.com/us/playlist/top-100-australia/pl.18be1cf04dfd4ffb9b6b0453e8fae8f1",
    "japan": "https://music.apple.com/us/playlist/top-100-japan/pl.043a2c9876114d95a4659988497567be",
    "spain": "https://music.apple.com/us/playlist/top-100-spain/pl.0d656d7feae64198bc5fb1b02786ed75",
    "france": "https://music.apple.com/us/playlist/top-100-france/pl.6e8cfd81d51042648fa36c9df5236b8d",
    "germany": "https://music.apple.com/us/playlist/top-100-germany/pl.c10a2c113db14685a0b09fa5834d8e8b",
    "south korea": "https://music.apple.com/us/playlist/top-100-south-korea/pl.d3d10c32fbc540b38e266367dc8cb00c",
    "armenia": "https://music.apple.com/us/playlist/top-100-armenia/pl.42abb2144d594137a8fb4d37a9f35b42",
    "costa rica": "https://music.apple.com/us/playlist/top-100-costa-rica/pl.7771c20fc0354f64a723ae9c11a4d5f5",
}

while oo1:
    a = input("Please pick Global or one country: ")
    if a.lower() in url_dict.keys():
        oo1=False
    else:
        print("Please, try another country")
print(f"Ok, you chose {a}, please wait few seconds")


URL = url_dict[a.lower()]

def get_html(url, params=None):
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="songs-list-row__song-container")
    track_names = []
    author_name = []
    song_rank = []
    for item in items:
        track_names.append(item.find("div", "songs-list-row__song-name").get_text())
        author_name.append(item.find("div", "songs-list-row__by-line").get_text())
        song_rank.append(item.find("div", "songs-list-row__rank").get_text())
    return track_names, author_name, song_rank


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print("Error")
        quit()
        
tracks, authors, ranks = parse()

for i in range(len(tracks)):
    while "  " in authors[i]:
        authors[i] = authors[i].replace("  ", " ")
    authors[i] = authors[i].replace("\n", "")
while oo:
    print("What do you want to know?\n 1 - top 100 \n 2 - top 10 \n 3 - choose 1 place \n 4 - choose 1 author\n 5 - quit")
    choise = int(input("Just type one number: "))
    if choise == 1:
        for i in range(100):
            print(f"{ranks[i]} {tracks[i]} \n  {authors[i]}")
        print(f"\nIf you want to continue type 'YES', \n or if you want to stop type 'NO'")
        yes_no=input()
        if yes_no=="NO":
            oo=False
            print("Hope that you enjoyed our service!")
    elif choise == 2:
        for i in range(10):
            print(f"{ranks[i]} {tracks[i]} \n  {authors[i]}")
        print(f"\nIf you want to continue type 'YES', \n or if you want to stop type 'NO'")
        yes_no=input()
        if yes_no=="NO":
            oo=False
            print("Hope that you enjoyed our service!")
    elif choise == 3:
        i = int(input("Please, write place in the top: ")) - 1
        if i <= 100:
            print(f"track: {tracks[i]} \nauthor: {authors[i]}")
            print(f"\nIf you want to continue type 'YES', \n or if you want to stop type 'NO'")
            yes_no=input()
            if yes_no=="NO":
                oo=False
            print("Hope that you enjoyed our service!")
        else:
            pass
    elif choise == 4:
        authors_copy=copy.copy(authors)
        tracks_copy=copy.copy(tracks)
        ranks_copy=copy.copy(ranks)
        list_of_looking_author_songs=[]
        list_of_looking_author_songs_ranks=[]
        look_for_author = input("Input author: ")+' '
        continuee=False
        print(authors)
        for _ in authors:
            if look_for_author==_:
                continuee=True
                list_of_looking_author_songs.append(tracks[authors.index(_)])
                list_of_looking_author_songs_ranks.append(ranks[authors.index(_)])
                authors.remove(_)
                tracks.remove(tracks[authors.index(_)])
                ranks.remove(ranks[authors.index(_)])
        authors=authors_copy
        tracks=tracks_copy
        ranks=ranks_copy
        print("Here is what were you looking for:")
        if continuee:
            for j in range(len(list_of_looking_author_songs)):
                print(f" {list_of_looking_author_songs_ranks[j]} {list_of_looking_author_songs[j]}")
        else:
            print(f" {look_for_author}is not in the top")
        
        print(f"\nIf you want to continue type 'YES', \n or if you want to stop type 'NO'")
        yes_no=input()
        if yes_no=="NO":
            oo=False
            print("Hope that you enjoyed our service!")
    elif choise == 5:
        oo=False
        print("Hope that you enjoyed our service!")
    else:
        print("Error! Please, try again")

