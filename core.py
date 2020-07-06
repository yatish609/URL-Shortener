import requests, validators

def createURL(originalURL: str) -> str:
    res = requests.post('https://api.short.cm/links', {
      'domain': 'tshbhardwaj725.shortcm.li',
      'originalURL': originalURL,
    }, headers = {'authorization': 'KtaIlSUyRvbYohxywUOv3FBC0ULEZu5I'}, json=True)

    res.raise_for_status()
    data = res.json()
    return data['shortURL']

def checkURL(url):
    valid=validators.url(url)
    return valid