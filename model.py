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

def isValidGenreStatusCode(submittedGenre):
    genres = {
        'action': 1,
        'adventure': 2,
        'cars': 3,
        'comedy': 4,
        'dementia': 5,
        'demons': 6,
        'mystery': 7,
        'drama': 8,
        'ecchi': 9,
        'fantasy': 10,
        'game': 11,
        'hentai': 12,
        'historical': 13,
        'horror': 14,
        'kids anime': 15,
        'kids': 15,
        'magic anime': 16,
        'magic': 16,
        'martial arts': 17,
        'mecha': 18,
        'music': 19,
        'musical': 19,
        'parody': 20
    }
    url = "https://api.jikan.moe/v3/genre/anime/"
    submittedGenre = submittedGenre.lower()
    submittedGenre = submittedGenre.strip()
    for genre in genres:
        if submittedGenre == genre:
            url += str(genres[genre])
            url += "/1"
    
    if (url != "https://api.jikan.moe/v3/genre/anime/"):
        response = requests.get(url)
        if int(response.status_code == 200):
            return True
        else:
            return False
    
    else:
        return False

def getAnimeGenreInfo(submittedGenre):
    genres = {
        'action': 1,
        'adventure': 2,
        'cars': 3,
        'comedy': 4,
        'dementia': 5,
        'demons': 6,
        'mystery': 7,
        'drama': 8,
        'ecchi': 9,
        'fantasy': 10,
        'game': 11,
        'hentai': 12,
        'historical': 13,
        'horror': 14,
        'kids anime': 15,
        'kids': 15,
        'magic anime': 16,
        'magic': 16,
        'martial arts': 17,
        'mecha': 18,
        'music': 19,
        'musical': 19,
        'parody': 20

    }
    url = "https://api.jikan.moe/v3/genre/anime/"
    submittedGenre = submittedGenre.lower()
    submittedGenre = submittedGenre.strip()
    for genre in genres:
        if submittedGenre == genre:
            url += str(genres[genre])
            url += "/1"
    response = requests.get(url)
    response = response.json()
    animes = response["anime"]
    returnData = []
    for anime in animes:
        returnData.append([anime["title"], anime["synopsis"]])
    return returnData
