import requests

def getAnimeInfo(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}&limit=5".format(anime))
    response = response.json()
    response = response["results"]
    returnData = []
    for singleResponse in response:
        gogoAnimeUrl = "https://www10.gogoanime.io/category/"
        title = singleResponse["title"]
        title = title.split()
        for x in range(len(title)):
            if (x == 0):
                gogoAnimeUrl += title[x]
            else:
                gogoAnimeUrl += '-'
                gogoAnimeUrl += title[x]

        returnData.append([singleResponse["title"], singleResponse["synopsis"], gogoAnimeUrl])
    return returnData

def isValidStatusCode(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
    if int(response.status_code) == 200:
        return True

    else:
        return False