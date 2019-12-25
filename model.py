import requests

def getAnimeInfo(anime):

def isValidStatusCode(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
    if int(reponse.status_code) == 200:
        return True

    else:
        return False