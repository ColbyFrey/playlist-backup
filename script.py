import requests


with open('playlists.txt', 'r') as file:
    for line in file:
        if line != "\n":
            req = requsts.get(line)
            print(req)
