import requests

def genGogoAnimeUrl(title):
    gogoAnimeUrl = "https://www10.gogoanime.io/category/"
    title = title.split()
    for x in range(len(title)):
        if (x == 0):
            gogoAnimeUrl += title[x]
        else:
            gogoAnimeUrl += '-'
            gogoAnimeUrl += title[x]
    
    return gogoAnimeUrl

def getAnimeInfo(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}&limit=30".format(anime))
    response = response.json()
    response = response["results"]
    returnData = []
    for singleResponse in response:
        title = singleResponse["title"]
        gogoAnimeUrl = genGogoAnimeUrl(title)
        score = singleResponse["score"] if singleResponse["score"] else 0
        dict = {
            'title': singleResponse['title'],
            'synopsis': singleResponse['synopsis'],
            'url': gogoAnimeUrl,
            'rating': score,
            'img': singleResponse["image_url"]
        }
        returnData.append(dict)
    return returnData

def isValidStatusCode(anime):
    response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
    statusCode = int(response.status_code)
    response = response.json()
    if (statusCode == 200 and len(response["results"]) > 0):
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
        'josei': 43,
        'kids anime': 15,
        'kids': 15,
        'magic anime': 16,
        'magic': 16,
        'martial arts': 17,
        'mecha': 18,
        'military': 38,
        'music': 19,
        'musical': 19,
        'parody': 20,
        'police': 39,
        'psychological': 40,
        'samurai': 21,
        'romance': 22,
        'school': 23,
        'sci fi': 24,
        'seinen': 42,
        'shoujo': 25,
        'shoujo ai': 26,
        'shounen': 27,
        'shounen ai': 28,
        'slice of life': 36,
        'space': 29,
        'sports': 30,
        'supernatural': 37,
        'super power': 31,
        'thriller': 41,
        'vampire': 32,
        'yaoi': 33,
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
        'josei': 43,
        'kids anime': 15,
        'kids': 15,
        'magic anime': 16,
        'magic': 16,
        'martial arts': 17,
        'mecha': 18,
        'military': 38,
        'music': 19,
        'musical': 19,
        'parody': 20,
        'police': 39,
        'psychological': 40,
        'samurai': 21,
        'romance': 22,
        'school': 23,
        'sci fi': 24,
        'seinen': 42,
        'shoujo': 25,
        'shoujo ai': 26,
        'shounen': 27,
        'shounen ai': 28,
        'slice of life': 36,
        'space': 29,
        'sports': 30,
        'supernatural': 37,
        'super power': 31,
        'thriller': 41,
        'vampire': 32,
        'yaoi': 33,
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
        gogoAnimeUrl = genGogoAnimeUrl(anime["title"])
        score = anime["score"] if anime["score"] else 0

        dict = {
            'title': anime['title'],
            'synopsis': anime['synopsis'],
            'url': gogoAnimeUrl,
            'rating': score,
            'img': anime["image_url"]
        }
        returnData.append(dict)

        returnData = sorted(returnData, key=lambda k: k['rating'], reverse = True)
    return returnData


