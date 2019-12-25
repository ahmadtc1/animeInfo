import requests

def getAnimeInfo(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
    response = response.json()
    response = response["results"]
    returnData = []
    for singleResponse in response:
        returnData.append(singleResponse["title"])
    return returnData



def isValidStatusCode(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
    if int(response.status_code) == 200:
        return True

    else:
        return False